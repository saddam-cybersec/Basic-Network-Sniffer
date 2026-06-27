#!/usr/bin/env python3
"""
Basic Network Sniffer
Captures and analyzes network packets using Scapy
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw, PcapWriter
import sys

# Global variable for writing packets to file
pcap_writer = None

def analyze_packet(packet):
    """
    Callback function for each captured packet.
    Extracts and displays packet information.
    """
    # Check if packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        
        # Determine the protocol
        protocol = "Unknown"
        payload_preview = ""
        
        if TCP in packet:
            protocol = "TCP"
            tcp_layer = packet[TCP]
            # Display source and destination ports
            sport = tcp_layer.sport
            dport = tcp_layer.dport
        elif UDP in packet:
            protocol = "UDP"
            udp_layer = packet[UDP]
            sport = udp_layer.sport
            dport = udp_layer.dport
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            # Get protocol number if not TCP/UDP/ICMP
            protocol = str(ip_layer.proto)
        
        # Extract payload if available
        if Raw in packet:
            raw_data = packet[Raw].load
            try:
                # Try to decode as text (up to 80 characters)
                payload_preview = raw_data[:80].decode('utf-8', errors='ignore')
                payload_preview = payload_preview.replace('\n', '\\n').replace('\r', '\\r')
            except:
                payload_preview = str(raw_data[:80])
        
        # Display packet information
        print(f"[+] {src_ip} --> {dst_ip} | Protocol: {protocol}")
        if payload_preview:
            print(f"    Payload: {payload_preview}...")
        print("-" * 70)
        
        # Write packet to pcap file for later analysis
        if pcap_writer:
            pcap_writer.write(packet)

def main():
    """
    Main function: starts the packet sniffer.
    """
    global pcap_writer
    
    print("=" * 70)
    print("        BASIC NETWORK SNIFFER - Cyber Security Tool")
    print("=" * 70)
    print("[*] Starting packet capture on interface: eth0")
    print("[*] Captured packets will be saved to: capture.pcap")
    print("[*] Press Ctrl+C to stop capturing")
    print("=" * 70)
    
    # Initialize pcap writer
    pcap_writer = PcapWriter("capture.pcap", append=False, sync=True)
    
    try:
        # Start sniffing on eth0 interface
        # count=0 means infinite capture until interrupted
        sniff(iface="eth0", prn=analyze_packet, count=0)
    except KeyboardInterrupt:
        print("\n[*] Capture stopped by user")
    except PermissionError:
        print("[!] Permission denied. Please run with sudo.")
        print("    sudo python3 network_sniffer.py")
    except Exception as e:
        print(f"[!] An error occurred: {e}")
    finally:
        if pcap_writer:
            pcap_writer.close()
            print(f"[*] Packets saved to capture.pcap")
        print("[*] Sniffer terminated")

if __name__ == "__main__":
    main()
