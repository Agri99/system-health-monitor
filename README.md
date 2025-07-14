# System Health Monitor
A simple Pyhton-based script that checks the system's health and logs key metrics such as :
- CPU usage
- RAM usage
- Disk usage
- Internet Connectivity
- Service Status

---

## Features
- Logs system resource usage with timestamp
- Saves logs to a local '.log' file
- Lightweight and easy to run
- Cross-platform (Windows/Linux)

---

## How to Run
1. Clone the repository:
'''bash

git clone
https://github.com/Agri99/system-health-monitor.git
cd system-health-monitor

3. (Optional but recomended) Set up a virtual environment:
'''bash

python -m venv
.\venv\Scripts\activate # On Windows
Source /venv/Script/activate # On Linux

4. Install Required Libraries:
'''bash

pip install -r requirenments.txt

5. Run the script:
'''bash

pyhton monitor.py

---

# Sample Output
=== 2025-07-09 23:06:34 ===
CPU Usage: 1.3%
RAM Usage: 41.3% (1343MB used of3921MB) 
Disk Usage: 26.8% (19GB used of 78GB)

Internet Connectivity: Online

Service 'sshd':, Running

---

## Version
- v1.0 - Basic Script with CPU, RAM, Disk Logging
- v1.1 - Added Internet check, Service Status check and Color-coded terminal output with 'colorama'

---

This is my first IT Support Project to demonstrate scripting, system monitoring, and basic Python automation.
#Agriana
