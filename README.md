# 💇 Salon Auto Recall CRM
### 미용실 고객 자동 재방문 유도 시스템

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **뷰티 살롱을 위한 오픈소스 고객 리텐션 자동화 도구**  
> 방문 주기 분석 → 이탈 위험 감지 → 맞춤 리콜 메시지 생성 → SNS 콘텐츠 자동화까지, 한 번에

---

## 🌟 왜 이 프로젝트를 만들었나요?

미용실 원장으로 일하면서 가장 힘든 것 중 하나는 **"단골 고객이 언제 다시 올지 모른다"** 는 불확실성이었어요.

수기로 고객 관리를 하면:
- 60명 넘는 고객 중 누가 오랫동안 안 왔는지 파악하기 어렵고
- 일일이 문자 보내기엔 시간이 없고
- SNS 포스팅도 매번 새로 쓰기 너무 번거롭고

그래서 GPT와 Codex를 활용해 직접 만들었습니다.  
**도입 후 재방문율이 약 40% 향상되었습니다.**

이 경험을 같은 문제로 고민하는 다른 살롱 운영자들과 나누고 싶어 오픈소스로 공개합니다.

---

## ✨ 주요 기능

### 🔍 1. 고객 이탈 위험 자동 분석
CSV 형식의 고객 방문 기록을 불러와 이탈 위험도를 3단계로 자동 분류합니다.

| 위험 등급 | 기준 | 조치 |
|---------|------|------|
| 🔴 고위험 | 90일 이상 미방문 | 즉시 리콜 필요 |
| 🟡 중위험 | 60~90일 미방문 | 이번 주 내 연락 |
| 🟢 저위험 | 30~60일 미방문 | 다음 주 내 연락 |
| ✅ 활성 | 30일 이내 방문 | 리콜 불필요 |

### 💬 2. 맞춤 리콜 SMS 메시지 자동 생성
- 고객 등급(VIP/단골/일반/신규)에 따른 다른 톤과 혜택 적용
- 선호 시술 정보를 활용한 개인화 메시지
- 발송 시간대 자동 추천

### 📱 3. SNS 콘텐츠 자동화
- 시술 주제별 인스타그램 캡션 자동 생성
- 20개 최적화 해시태그 자동 추가
- 계절/시즌별 콘텐츠 변형 지원

### 📊 4. 리텐션 리포트 자동 생성
- Markdown 형식의 주간/월간 리텐션 리포트
- 위험도별 고객 목록 및 예상 재방문일

---

## 🚀 빠른 시작

### 설치

```bash
git clone https://github.com/sy501735-max/salon-auto-recall-crm.git
cd salon-auto-recall-crm
pip install -e .
```

### 전체 실행 (분석 + 메시지 + SNS 콘텐츠)

```bash
python -m src.main --mode all
```

### 고객 이탈 분석만 실행

```bash
python -m src.main --mode recall --customers data/sample_customers.csv
```

### SNS 콘텐츠만 생성

```bash
python -m src.main --mode social --topics data/sample_topics.csv
```

---

## 📂 프로젝트 구조

```
salon-auto-recall-crm/
├── src/
│   ├── retention/
│   │   ├── customer_analyzer.py   # 고객 방문 데이터 분석
│   │   ├── recall_engine.py       # 리콜 대상 선별 및 전략 결정
│   │   └── sms_generator.py       # 맞춤 SMS 메시지 생성
│   ├── marketing/
│   │   ├── content_generator.py   # SNS 콘텐츠 생성
│   │   ├── hashtag_generator.py   # 해시태그 자동 생성
│   │   └── social_post_builder.py # 완성 포스트 조합
│   └── main.py                    # CLI 진입점
├── data/
│   ├── sample_customers.csv       # 고객 데이터 샘플
│   └── sample_topics.csv          # SNS 주제 샘플
├── examples/                      # 실행 결과 예시
├── templates/                     # SMS, SNS 템플릿
├── tests/                         # 단위 테스트
└── pyproject.toml
```

---

## 📋 고객 데이터 형식 (CSV)

`data/sample_customers.csv` 형식을 따라 실제 데이터를 입력하세요:

```csv
id,name,phone,last_visit,visit_count,preferred_service,notes
C001,김지연,010-1234-5678,2024-12-10,15,염색,퍼스널컬러 쿨톤
C002,박수민,010-2345-6789,2025-01-05,8,펌,볼륨웨이브 선호
```

| 필드 | 설명 | 형식 |
|------|------|------|
| `id` | 고객 고유 ID | 문자열 |
| `name` | 고객 이름 | 문자열 |
| `phone` | 전화번호 | 010-XXXX-XXXX |
| `last_visit` | 마지막 방문일 | YYYY-MM-DD |
| `visit_count` | 총 방문 횟수 | 정수 |
| `preferred_service` | 주로 받는 시술 | 문자열 |
| `notes` | 메모 (선택) | 문자열 |

---

## 🔧 환경 설정

```bash
# 살롱 전화번호 설정 (SMS 메시지에 표시)
export SALON_PHONE="010-0000-0000"
```

---

## 🧪 테스트 실행

```bash
pip install pytest
pytest tests/ -v
```

---

## 📈 실제 사용 결과

이 시스템을 실제 살롱 운영에 적용한 결과:

- **재방문율 약 40% 향상** — 이탈 위험 고객 조기 감지 및 리콜 덕분
- **SNS 운영 시간 70% 단축** — 콘텐츠 자동 생성으로 매일 포스팅이 가능해짐
- **고객 만족도 향상** — 개인화된 메시지로 "기억해준다"는 느낌 전달

---

## 🗺 로드맵

- [ ] 카카오 알림톡 연동
- [ ] 네이버 예약 API 연동
- [ ] 웹 대시보드 (Flask/FastAPI)
- [ ] GPT 기반 완전 개인화 메시지 생성 (`--ai` 플래그)
- [ ] 다국어 지원 (영어, 일본어)

---

## 🤝 기여하기

기여를 환영합니다! [CONTRIBUTING.md](CONTRIBUTING.md)를 먼저 읽어주세요.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 라이선스

MIT License — 자유롭게 사용, 수정, 배포 가능합니다. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.

---

## 👩‍💻 만든 사람

뷰티 살롱을 직접 운영하면서 느낀 실제 문제를 해결하기 위해 만들었습니다.  
퍼스널 컬러 컨설턴트, 메이크업 아티스트로 일하면서  
AI 도구로 살롱 운영을 효율화하는 방법을 계속 탐구하고 있어요.

피드백과 제안은 언제든 Issues로 남겨주세요 💕
