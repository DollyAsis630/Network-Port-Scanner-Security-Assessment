# Network Port Scanning and Security Assessment

## Project Overview
The Network Port Scanning and Security Assessment project demonstrates how Python and Nmap can be used to scan a system for open ports and document the results. It provides a basic introduction to network reconnaissance and security assessment.

## Objectives
- Identify open ports on an authorized target
- Understand basic network port scanning.
- Use Python to automate port-scanning tasks.
- Use Nmap to perform network scans.
- Record and review scan results.

## Technologies Used
- **Python:** Implements the port-scanning functionality.
- **Nmap:** Performs network scanning and identifies open ports.
- **Visual Studio Code:** Used to develop and run the project.

## Project Files
- `scanner.py` — Python port scanner.
- `security_assessment.py` — Security assessment script.
- `scan_results.csv` — Recorded scan results.
- `nmap_results.txt` — Nmap scan output.
- `security_report.txt` — Security assessment report.
- `Network_Port_Scanner_Report.md` — Project report.
- `screenshots/` — Screenshots showing project execution and results.

## Testing
The scanner was tested against the local system (`127.0.0.1`). Port `8000` was detected as open while a local Python HTTP server was running.

An open port does not automatically indicate a security vulnerability. Further investigation is required to determine whether a service is exposed or misconfigured.

## How to Run
1. Install Python.
2. Install Nmap and ensure it is available on your system.
3. Open the project folder in Visual Studio Code.
4. Run the Python scanner:

   ```bash
   python scanner.py
   ```

5. Review the generated scan results.

Follow the commands and configuration defined in the actual project files if they differ from these general instructions.

## Security and Ethical Use
Use this project only on your own systems or on networks for which you have explicit permission to conduct security testing. Do not scan unauthorized targets.

## Learning Outcomes
- Basic understanding of TCP port scanning.
- Practical experience using Python and Nmap.
- Recording and reviewing scan results.
- Introduction to network security assessment.
