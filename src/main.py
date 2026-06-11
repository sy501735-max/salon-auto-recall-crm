from datetime import datetime

def days_since_visit(last_visit):
    today = datetime.today()
    visit = datetime.strptime(last_visit, "%Y-%m-%d")
    return (today - visit).days

def classify_customer(days):
    if days >= 90:
        return "High Priority"
    elif days >= 60:
        return "Medium Priority"
    elif days >= 30:
        return "Low Priority"
    return "Active"

customer = {
    "name": "John",
    "last_visit": "2026-03-01"
}

days = days_since_visit(customer["last_visit"])

print(customer["name"])
print(days)
print(classify_customer(days))
