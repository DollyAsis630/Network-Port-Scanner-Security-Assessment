
import socket
import csv
from datetime import datetime, timezone

# Scanned on own computer
TARGET = "127.0.0.1"

PORTS = [21, 22, 80, 443, 8000, 8080]
TIMEOUT_SECONDS = 0.5

results = []

def identify_service(port):
    """Identify a few common services by port number."""
    services = {
        21: "FTP (possible)",
        22: "SSH (possible)",
        80: "HTTP (possible)",
        443: "HTTPS (possible)",
        8000: "HTTP alternate (possible)",
        8080: "HTTP proxy/alternate (possible)"
    }
    return services.get(port, "Unknown")

def check_http_response(port):
    """Try a basic HTTP request on an open local port."""
    try:
        with socket.create_connection(
            (TARGET, port), timeout=TIMEOUT_SECONDS
        ) as sock:
            sock.settimeout(TIMEOUT_SECONDS)
            sock.sendall(
                b"GET / HTTP/1.0\r\nHost: localhost\r\n\r\n"
            )
            response = sock.recv(1024)
            first_line = response.split(b"\r\n", 1)[0]
            return first_line.decode("utf-8", errors="replace")
    except (OSError, TimeoutError):
        return "No HTTP response detected"

print("Localhost Port Scanner")
print("-" * 40)

for port in PORTS:
    service = identify_service(port)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT_SECONDS)
            status = sock.connect_ex((TARGET, port))

        if status == 0:
            state = "open"
        else:
            state = "not open"

    except OSError as exc:
        state = f"error: {type(exc).__name__}"

    http_response = ""
    if state == "open" and port in [80, 8000, 8080]:
        http_response = check_http_response(port)

    print(
        f"{TARGET}:{port} | {state} | {service}"
        + (f" | {http_response}" if http_response else "")
    )

    results.append([
        datetime.now(timezone.utc).isoformat(),
        TARGET,
        port,
        state,
        service,
        http_response
    ])

with open("scan_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "timestamp_utc",
        "host",
        "port",
        "state",
        "service_guess",
        "http_response"
    ])
    writer.writerows(results)

print("-" * 40)
print("Saved scan_results.csv")
