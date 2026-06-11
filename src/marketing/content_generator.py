"""
content_generator.py
SNS 포스팅용 콘텐츠를 주제 데이터 기반으로 자동 생성합니다.
"""

import csv
from pathlib import Path
from datetime import datetime


# 시술별 콘텐츠 뱅크
CONTENT_BANK = {
    "펌": {
        "hook": ["이 펌 스타일, 올봄 대세예요 🌸", "모발 손상 없이 예쁜 웨이브 💕", "내 머리에 맞는 펌 찾기"],
        "body": "건강한 모발을 유지하면서도 아름다운 웨이브를 만들 수 있어요. 모발 상태에 따라 맞춤 시술을 추천해드립니다.",
        "cta": "📲 DM으로 상담 문의 주세요!",
    },
    "염색": {
        "hook": ["이 컬러, 올해 가장 핫해요 🎨", "나에게 맞는 색 찾는 법", "염색 후 색이 금방 빠진다면?"],
        "body": "퍼스널 컬러에 맞는 염색 컬러를 선택하면 피부 톤이 훨씬 밝아 보여요. 상담을 통해 나만의 컬러를 찾아보세요.",
        "cta": "💬 컬러 상담 예약하기",
    },
    "커트": {
        "hook": ["얼굴형에 맞는 커트 스타일 🪄", "이 커트 하나로 분위기가 달라져요", "자르고 나서 후회 없는 커트"],
        "body": "얼굴형과 라이프스타일에 맞는 커트를 제안해드려요. 매일 아침 5분이면 완성되는 스타일링으로 바꿔드릴게요.",
        "cta": "📅 예약은 프로필 링크에서",
    },
    "두피케어": {
        "hook": ["두피가 건강해야 모발도 건강해요 🌿", "탈모 걱정 있으신가요?", "두피 타입별 관리법"],
        "body": "스트레스와 환경 변화로 두피 트러블이 많아지고 있어요. 전문적인 두피 진단으로 내 두피 타입에 맞는 관리를 시작해보세요.",
        "cta": "🔍 무료 두피 진단 상담 신청",
    },
    "클리닉": {
        "hook": ["손상 모발, 집에서 케어하는 법 💆", "드라이기 때문에 모발 손상?", "윤기 있는 모발의 비결"],
        "body": "염색과 펌을 반복하다 보면 모발이 손상되기 쉬워요. 딥 클리닉으로 모발에 영양을 채우고 건강하게 회복시켜 드릴게요.",
        "cta": "✨ 클리닉 시술 문의하기",
    },
}

DEFAULT_CONTENT = {
    "hook": ["오늘의 살롱 스타일 ✨", "뷰티 꿀팁 공유해요", "이번 주 인기 시술"],
    "body": "건강하고 아름다운 헤어를 위해 항상 최선을 다하겠습니다.",
    "cta": "📞 예약 문의는 DM으로!",
}


class ContentGenerator:
    """CSV 주제 파일 기반 SNS 콘텐츠 자동 생성"""

    def __init__(self, topics_csv: str = None):
        self.topics_csv = Path(topics_csv) if topics_csv else None
        self._topics: list[dict] = []

    def _load_topics(self) -> list[dict]:
        """주제 CSV 로드"""
        if not self.topics_csv or not self.topics_csv.exists():
            # 파일 없으면 기본 주제 사용
            return [
                {"topic": "펌", "season": "봄", "target": "20-30대"},
                {"topic": "염색", "season": "봄", "target": "30-40대"},
                {"topic": "커트", "season": "사계절", "target": "전체"},
            ]

        topics = []
        with open(self.topics_csv, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                topics.append({k: v.strip() for k, v in row.items()})
        return topics

    def _match_content(self, topic: str) -> dict:
        """주제에 맞는 콘텐츠 뱅크 반환"""
        for key, content in CONTENT_BANK.items():
            if key in topic:
                return content
        return DEFAULT_CONTENT

    def generate_post(self, topic_row: dict) -> dict:
        """단일 주제로 SNS 포스트 생성"""
        topic = topic_row.get("topic", "")
        season = topic_row.get("season", "")
        target = topic_row.get("target", "")

        content = self._match_content(topic)

        # 여러 훅 중 첫 번째 선택 (실제 서비스에선 A/B 테스트 가능)
        hook = content["hook"][0]
        if season:
            hook = f"[{season}] {hook}"

        return {
            "topic": topic,
            "season": season,
            "target": target,
            "hook": hook,
            "body": content["body"],
            "cta": content["cta"],
            "generated_at": datetime.now().strftime("%Y-%m-%d"),
        }

    def generate_all(self) -> list[dict]:
        """전체 주제 목록으로 포스트 일괄 생성"""
        self._topics = self._load_topics()
        return [self.generate_post(t) for t in self._topics]
