# PythonLogAnalyzer
# Python Security Log Analyzer

A lightweight Python-based security log analysis tool designed to detect suspicious authentication activity such as repeated failed login attempts.  
This project focuses on building security-oriented thinking using simple Python fundamentals.

---
## Project Objective

The goal of this project is to practice:

- Log analysis fundamentals
- Basic threat detection logic
- Security-first reasoning
- Python scripting in a cybersecurity context

This project is intentionally kept simple and extensible, serving as a foundation for future enhancements such as risk scoring, alerting, and automation.

---

## Features

- Reads authentication log files
- Identifies failed login attempts
- Filters potentially suspicious events
- Outputs results to the terminal

---

## Project Structure# Python Security Log Analyzer

A lightweight Python-based security log analysis tool designed to detect suspicious authentication activity such as repeated failed login attempts.  
This project focuses on building security-oriented thinking using simple Python fundamentals.

---

## Project Objective

The goal of this project is to practice:

- Log analysis fundamentals
- Basic threat detection logic
- Security-first reasoning
- Python scripting in a cybersecurity context

This project is intentionally kept simple and extensible, serving as a foundation for future enhancements such as risk scoring, alerting, and automation.

---

## Features

- Reads authentication log files
- Identifies failed login attempts
- Filters potentially suspicious events
- Outputs results to the terminal

---

## Project Structure

python-security-log-analyzer/
│
├── analyzer.py
├── sample_logs/
│ └── auth.log
└── README.md

---

## Sample Log Format

The analyzer currently supports logs in the following format:
2026-01-01 01:12:45 FAILED_LOGIN user=admin ip=192.168.1.23
2026-01-01 01:13:02 FAILED_LOGIN user=admin ip=192.168.1.23
2026-01-01 09:00:01 SUCCESS_LOGIN user=vikrant ip=10.0.0.5

This onal for learning and experimentation.

---

## Requirements

- Python 3.x
- No external dependencies

---

## Future Enhancements

Planned improvements include:

- Time-based anomaly detection
- Enhanced risk scoring logic
- JSON report generation
- Support for real system logs
- Alerting and automation hooks

---

## Disclaimer

This project uses sample log data only.  
No real credentials, sensitive information, or production logs are included.

