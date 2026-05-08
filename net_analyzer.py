#%%writefile net_analyzer.py  
import subprocess
import time
import os
import signal
import sys

# Ensure the script is run with root/sudo privileges
if os.geteuid() != 0:
    print("Permission Denied: Please run this script with sudo.")
    sys.exit(1)

target = "www.inria.fr"
print("Starting background packet capture using tcpdump...")

# -U forces packet-buffered output
tcpdump_cmd = ["tcpdump", "-i", "any", "icmp", "-n", "-U", "-w", "python_trace.pcap"]
tcpdump_proc = subprocess.Popen(tcpdump_cmd)

time.sleep(2)

print(f"Running network diagnostics to {target}...")

with open("python_net_trace.txt", "w") as file_out:
    
    print("Executing ping...")
    # shell=True resolves the Colab system path issues
    subprocess.run(f"ping -c 5 {target}", shell=True, stdout=file_out)
    
    file_out.write("\n" + "="*40 + "\n")
    
    print("Executing traceroute...")
    subprocess.run(f"traceroute {target}", shell=True, stdout=file_out)

time.sleep(2)

# CRITICAL FIX: Send SIGINT (Ctrl+C equivalent) for a graceful shutdown
tcpdump_proc.send_signal(signal.SIGINT)

# Wait for tcpdump to write the PCAP headers and close the file
tcpdump_proc.wait()

# CRITICAL FIX: Force the Colab filesystem to flush memory to disk
os.sync()
time.sleep(2)

print("Automation Complete!")
print("Check python_net_trace.txt for the terminal output.")
print("You can now safely download python_trace.pcap to open in Wireshark.")