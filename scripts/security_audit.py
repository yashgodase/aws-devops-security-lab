import os
import platform
import subprocess

print("===== LINUX SECURITY AUDIT ======")

print("\n1.SYSTEM INFORMATION")
print(platform.uname())

print("\n2.CURRENT USER")
print(os.environ.get("USER", "UNKNOWN"))

print("\n3.OPEN NETWORK PORTS")
subprocess.run(["ss", "-tuln"])

print("n4.DISK USAGE")
subprocess.run(["df", "-h"])

print("\n===== AUDIT COMPLETED =====")

