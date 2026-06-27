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

Press Ctrl+C to stop capturing.

⚠️ Legal Disclaimer
This tool is designed exclusively for educational purposes and authorized network testing. You must have explicit written permission to sniff traffic on any network you do not own. Unauthorized interception of network traffic is illegal in most jurisdictions. Use responsibly.


**For the Keylogger README (`Keylogger-Project/README.md`):**

```markdown
# ⚠️ Basic Keylogger Simulation - EDUCATIONAL USE ONLY

**Author:** Saddam Hussain
**Internship:** Arch Technologies (Cyber Security)

## Overview
This script demonstrates how keyboard listeners work in Python using the `pynput` library. It logs keystrokes locally to a text file (`key_log.txt`) with timestamps and stops when the `ESC` key is pressed.

## Features
- Captures alphanumeric and special keys (Enter, Backspace, Space, etc.).
- Logs every keystroke with a timestamp.
- Graceful exit using the `ESC` key.

## Installation & Usage
```bash
# Install dependency
pip install -r requirements.txt

# Run the script (No sudo required)
python3 keylogger.py

Press ESC to stop logging.

⚠️ CRITICAL LEGAL WARNING
This script is created strictly for learning and testing on your own personal devices.

DO NOT install or run this on any device without the explicit, written consent of the owner.

Unauthorized keystroke logging is a federal crime in many countries (violating privacy laws, GDPR, and the Computer Fraud and Abuse Act).

The author and Arch Technologies take zero responsibility for any malicious or illegal use of this code.


---

### Step 5: Upload (Push) Them Separately

Open your terminal and run these commands **separately** for each folder:

**For the Network Sniffer:**
```bash
cd /path/to/Network-Sniffer-Project
git init
git add .
git commit -m "Initial commit: Basic Network Sniffer for Cyber Security Internship"
git remote add origin https://github.com/saddam-cybersec/Network-Sniffer-Python.git
git branch -M main
git push -u origin main

````
