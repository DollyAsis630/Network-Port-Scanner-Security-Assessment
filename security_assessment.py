
import csv
from datetime import datetime

CSV_FILE = "scan_results.csv"
REPORT_FILE = "security_report.txt"

# Ports that deserve a closer look if they are open
PORTS_TO_REVIEW = {
    21: "FTP: check whether encryption is used",
    22: "SSH: check authentication and configuration",
    80: "HTTP: check whether unencrypted web traffic is appropriate",
    443: "HTTPS: check TLS configuration",
    8000: "Alternate HTTP port: confirm whether the service is needed",
    8080: "Alternate HTTP/proxy port: confirm whether the service is needed",
}

try:
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
except FileNotFoundError:
    print(f"Error: {CSV_FILE} was not found.")
    print("Run scanner.py first, in this same folder.")
    raise SystemExit(1)

open_ports = []
review_items = []

for row in rows:
    port = int(row["port"])
    state = row["state"].strip().lower()
    service = row.get("service_guess", "Unknown")

    if state == "open":
        open_ports.append(port)
        review_items.append(
            f"Port {port} is open. Service hint: {service}. "
            f"Review: {PORTS_TO_REVIEW.get(port, 'Confirm the service is needed.')}"
        )

lines = [
    "NETWORK PORT SCANNER - SECURITY ASSESSMENT",
    "=" * 48,
    f"Report generated: {datetime.now().astimezone().isoformat()}",
    "Target: 127.0.0.1 (localhost)",
    f"Ports tested: {len(rows)}",
    f"Open ports found: {len(open_ports)}",
    "",
    "OPEN PORTS",
    "-" * 48,
]

if open_ports:
    lines.extend(f"Port {port}" for port in open_ports)
else:
    lines.append("No open ports were detected in this scan.")

lines.extend(["", "RECOMMENDATIONS", "-" * 48])

if review_items:
    lines.extend(f"- {item}" for item in review_items)
else:
    lines.append("- No open ports were found to review.")

lines.extend([
    "",
    "LIMITATIONS",
    "-" * 48,
    "An open port is not automatically a vulnerability.",
    "Service names based only on port numbers are guesses.",
    "This report is a basic review, not a complete security audit.",
])

with open(REPORT_FILE, "w", encoding="utf-8") as file:
    file.write("\n".join(lines) + "\n")

print("\n".join(lines))
print(f"\nSaved report to {REPORT_FILE}")
