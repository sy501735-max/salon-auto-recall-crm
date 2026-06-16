# 💇 Salon Auto Recall CRM

### Open Source Customer Retention Automation Framework

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)


<p align="center">

<strong>
Turn customer visit history into automated retention workflows.
</strong>

<br />

Analyze visits → Detect retention risks → Generate personalized messages → Automate marketing content

</p>


---

# 🚀 What is Salon Auto Recall CRM?

**Salon Auto Recall CRM** is an open-source customer retention automation framework designed for appointment-based businesses.

It transforms customer visit history into actionable retention workflows without requiring expensive CRM SaaS platforms.

The system helps businesses answer:

- Who should we contact today?
- Which customers may stop returning?
- What message should we send?
- How can repetitive marketing tasks be automated?


Customer Visit Data
|
v
Retention Risk Analysis
|
v
Customer Segmentation
|
v
Action Generator
|
+---- Personalized Messages
|
+---- Marketing Content
|
+---- Retention Reports


Although originally designed for beauty salons, the architecture is intended to be extended for:

- 💇 Beauty salons
- 🏥 Clinics
- 🧘 Studios
- 🏪 Local service businesses


---

# ✨ Why this project?

Many small businesses collect customer data,
but often lack simple tools to turn that data into retention actions.

Existing CRM solutions are often:

- Expensive
- Over-complicated
- Dependent on external platforms

This project provides a lightweight,
self-hosted automation foundation focused on:

- Customer retention
- Personalized communication
- Marketing workflow automation


---

# 🎯 Project Goals

- Local-first CRM automation
- Explainable retention logic
- Modular architecture
- Easy customization
- Community-driven extensions


---

# ⚙️ Features


## 🔍 1. Customer Retention Risk Analysis

Analyzes customer visit history and classifies retention risk.

| Segment | Condition | Suggested Action |
|---------|-----------|------------------|
| 🔴 High Risk | 90+ days inactive | Immediate outreach |
| 🟡 Medium Risk | 60~90 days inactive | Contact soon |
| 🟢 Low Risk | 30~60 days inactive | Monitor |
| ✅ Active | Within 30 days | No action needed |


The scoring logic is designed to be:

- Simple
- Explainable
- Easy to customize


---

## 💬 2. Personalized Message Generator

Generates customer-specific retention messages.

Supports:

- Customer segmentation
- Preferred service information
- Custom templates
- Business-specific tone adjustment


Example:

```text
Hi {name},

It's been {days} days since your last {service}.
We would love to welcome you back.


## 🏗 Architecture
