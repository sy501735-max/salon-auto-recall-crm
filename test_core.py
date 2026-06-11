"""
tests/test_core.py
핵심 기능 단위 테스트
"""

import pytest
import tempfile
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.retention.customer_analyzer import CustomerAnalyzer
from src.retention.recall_engine import RecallEngine
from src.retention.sms_generator import SMSGenerator


SAMPLE_CSV_CONTENT = """id,name,phone,last_visit,visit_count,preferred_service,notes
C001,테스트고객1,010-1111-2222,2024-11-01,10,염색,VIP 고객
C002,테스트고객2,010-3333-4444,2025-04-01,5,펌,단골
C003,테스트고객3,010-5555-6666,2025-05-25,2,커트,신규
"""


@pytest.fixture
def sample_csv(tmp_path):
    csv_file = tmp_path / "test_customers.csv"
    csv_file.write_text(SAMPLE_CSV_CONTENT, encoding="utf-8")
    return str(csv_file)


class TestCustomerAnalyzer:
    def test_load_and_analyze(self, sample_csv):
        analyzer = CustomerAnalyzer(sample_csv)
        report = analyzer.analyze()

        assert report["total_customers"] == 3
        assert "at_risk_count" in report
        assert "avg_visit_interval_days" in report
        assert "customers" in report

    def test_risk_assessment(self, sample_csv):
        analyzer = CustomerAnalyzer(sample_csv)
        report = analyzer.analyze()

        # 2024-11-01 방문 고객은 고위험이어야 함
        customers_by_name = {c["name"]: c for c in report["customers"]}
        assert customers_by_name["테스트고객1"]["risk_level"] == "high"

    def test_markdown_output(self, sample_csv):
        analyzer = CustomerAnalyzer(sample_csv)
        report = analyzer.analyze()
        md = analyzer.to_markdown(report)

        assert "# 고객 방문 분석 리포트" in md
        assert "전체 고객 수" in md

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            analyzer = CustomerAnalyzer("nonexistent.csv")
            analyzer.analyze()


class TestRecallEngine:
    def test_generate_recall_list(self):
        engine = RecallEngine()
        sample_customers = [
            {
                "id": "C001", "name": "VIP고객", "phone": "010-0000-0001",
                "last_visit": "2024-11-01", "visit_count": 12,
                "preferred_service": "염색", "risk_level": "high",
                "days_since_visit": 200, "next_expected_visit": "2025-02-19",
            },
            {
                "id": "C002", "name": "신규고객", "phone": "010-0000-0002",
                "last_visit": "2025-05-25", "visit_count": 1,
                "preferred_service": "커트", "risk_level": "active",
                "days_since_visit": 17, "next_expected_visit": "2025-07-24",
            },
        ]

        recall_list = engine.generate_recall_list(sample_customers)

        # 활성 고객은 제외됨
        assert len(recall_list) == 1
        assert recall_list[0]["name"] == "VIP고객"
        assert recall_list[0]["tier"] == "vip"

    def test_priority_ordering(self):
        engine = RecallEngine()
        customers = [
            {
                "id": "C001", "name": "일반고객", "visit_count": 2,
                "preferred_service": "커트", "risk_level": "medium",
                "days_since_visit": 65,
            },
            {
                "id": "C002", "name": "VIP고객", "visit_count": 15,
                "preferred_service": "염색", "risk_level": "high",
                "days_since_visit": 120,
            },
        ]
        recall_list = engine.generate_recall_list(customers)
        assert recall_list[0]["name"] == "VIP고객"


class TestSMSGenerator:
    def test_generate_message(self):
        gen = SMSGenerator(salon_name="테스트살롱", salon_phone="010-9999-8888")
        customer = {
            "id": "C001", "name": "김지연", "phone": "010-1234-5678",
            "days_since_visit": 100, "preferred_service": "염색",
            "tier": "vip",
            "strategy": {"tone": "intimate", "urgency": "high",
                         "offer": "VIP 10% 할인", "channel": "sms"},
        }
        result = gen.generate(customer)

        assert result["name"] == "김지연"
        assert "김지연" in result["message"]
        assert result["urgency"] == "high"

    def test_batch_generate(self):
        gen = SMSGenerator()
        customers = [
            {
                "id": f"C00{i}", "name": f"고객{i}", "phone": f"010-000{i}-0000",
                "days_since_visit": 60, "preferred_service": "커트",
                "tier": "regular",
                "strategy": {"tone": "friendly", "urgency": "medium",
                             "offer": "혜택", "channel": "sms"},
            }
            for i in range(3)
        ]
        messages = gen.batch_generate(customers)
        assert len(messages) == 3

    def test_markdown_output(self):
        gen = SMSGenerator()
        messages = [
            {
                "name": "테스트", "phone": "010-0000-0000",
                "message": "테스트 메시지", "channel": "sms",
                "urgency": "high", "tier": "vip",
                "send_at": "오늘 오전 10시",
            }
        ]
        md = gen.to_markdown(messages)
        assert "# 리콜 SMS 메시지 목록" in md
