#!/bin/bash

# Ensure the script is run with root/sudo privileges
if [ "$EUID" -ne 0 ]; then 
    echo "Permission Denied: Please run this script with sudo."
    exit 1
fi

TARGET="www.inria.fr"
echo "Starting background packet capture using tcpdump..."

# Start tcpdump in the background
# -U forces packet-buffered output to prevent pcap corruption
tcpdump -i any icmp -n -U -w trace.pcap &
TCPDUMP_PID=$!

sleep 2

echo "Running ping to $TARGET..."
ping -c 5 $TARGET > network_trace.txt

echo "Running traceroute to $TARGET..."
traceroute $TARGET >> network_trace.txt

sleep 2

# CRITICAL FIX: Send SIGINT (Ctrl+C equivalent) for a graceful shutdown
kill -SIGINT $TCPDUMP_PID

# Wait for tcpdump to fully close and write pcap headers
sleep 2

# CRITICAL FIX: Force the Colab filesystem to flush the file to disk
sync

echo "Automation Complete! Check network_trace.txt for the terminal output."
echo "You can now safely download trace.pcap for Wireshark."