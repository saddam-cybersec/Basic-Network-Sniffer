# Basic Network Sniffer - Educational Tool

**Author:** Saddam Hussain  
**Internship:** Arch Technologies (Cyber Security)

## Overview

This Python script captures live network traffic using the Scapy library. It extracts source/destination IPs, identifies protocols (TCP/UDP/ICMP), previews payload data, and saves packets to a `.pcap` file for analysis in Wireshark.

## Features

- Real-time packet capture on a specified network interface.
- Protocol detection and payload preview.
- Saves captured data to `capture.pcap` for offline forensic analysis.

## Installation & Usage

````bash
# Install dependency
pip install -r requirements.txt

# Run with sudo (required for packet sniffing)
sudo python3 network_sniffer.py
````

Press Ctrl+C to stop capturing.

#⚠️ Legal Disclaimer
This tool is designed exclusively for educational purposes and authorized network testing. You must have explicit written permission to sniff traffic on any network you do not own. Unauthorized interception of network traffic is illegal in most jurisdictions. Use responsibly.

