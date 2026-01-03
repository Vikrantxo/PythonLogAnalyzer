# Python Log Analyzer

failed_ips = {}

with open("PythonLogAnalyzer/Sample_log.txt", "r") as content:
    for line in content:
        if "FAILED_LOGIN" in line:
            parts = line.strip().split()

            for part in parts:
                if part.startswith("ip="):
                    ip = part.split("=")[1]


                    if ip in failed_ips:
                        failed_ips[ip] += 1
                    else:
                        failed_ips[ip] = 1

# Print the dictionary
print("\nFailed login attempts per IP:\n")

for ip, count in failed_ips.items():
    print(f"{ip} -> {count} failed attempts")