# Network Traffic Analysis

This project automates network diagnostics and captures network traffic using Python, Bash, and packet analysis tools. It simulates a real-world workflow for analyzing network behavior and troubleshooting connectivity in a Linux environment.

---

## Features

- Automated network diagnostics using `ping` and `traceroute`  
- Packet capture using `tcpdump`  
- Generation of `.pcap` files for Wireshark analysis  
- Logging of network output to `.txt` files  
- Safe handling of background processes and packet capture termination  

---

## Tech Stack

- Python  
- Bash  
- Linux  
- tcpdump  
- Wireshark  

---

## How It Works

1. Starts packet capture using `tcpdump` in the background  
2. Runs network diagnostics (`ping` and `traceroute`)  
3. Saves output to a `.txt` log file  
4. Stops packet capture safely using signals  
5. Outputs a `.pcap` file for analysis in Wireshark  

---

## Results

- Successfully automated network diagnostics using Python and Bash  
- Resolved environment dependency issues by installing required networking tools (`tcpdump`, `ping`, `traceroute`)  
- Captured live ICMP traffic and generated `.pcap` files for analysis in Wireshark  
- Produced structured `.txt` logs containing ping and traceroute outputs  
- Demonstrated ability to troubleshoot, configure, and execute network analysis in a Linux environment  
- Simulated a real-world workflow for network debugging and traffic inspection  

---

## Challenges & Solutions

- **Issue:** Required networking tools were not available in the environment  
  **Solution:** Installed dependencies using `apt-get`, enabling full script execution  

- **Issue:** Ensuring proper packet capture without corruption  
  **Solution:** Used tcpdump flags (`-U`) and controlled shutdown using signals (SIGINT) to safely stop capture  

This reflects real-world problem-solving in system and network environments.

---

## How to Run

### Install dependencies
```bash
sudo apt-get update
sudo apt-get install tcpdump traceroute iputils-ping -y