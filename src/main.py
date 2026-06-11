from datetime import datetime

def days_since_visit(last_visit):
    """마지막 방문일로부터 경과일 계산"""
    today = datetime.today()
    visit_date = datetime.strptime(last_visit, "%Y-%m-%d")
    return (today - visit_date).days


def classify_customer(days):
    """고객 우선순위 분류"""

    if days >= 90:
        return "High Priority"

    elif days >= 60:
        return "Medium Priority"

    elif days >= 30:
        return "Low Priority"

    return "Active"


def generate_message(name, days):
    """재방문 유도 메시지 생성"""

    return f"""
안녕하세요 {name}님 😊

마지막 방문 후 {days}일이 지났습니다.

스타일 관리가 필요한 시점입니다.
예약 시 특별 혜택을 제공해드립니다.

감사합니다.
"""


def main():

    customer = {
        "name": "Kim",
        "last_visit": "2026-03-01",
        "service": "Haircut"
    }

    days = days_since_visit(customer["last_visit"])
    priority = classify_customer(days)

    print("=" * 50)
    print("Salon Auto Recall CRM")
    print("=" * 50)

    print(f"Customer: {customer['name']}")
    print(f"Days Since Visit: {days}")
    print(f"Priority: {priority}")

    print("\nGenerated Message")
    print(generate_message(customer["name"], days))


if __name__ == "__main__":
    main()
