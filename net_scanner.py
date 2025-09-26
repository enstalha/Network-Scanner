"""
Network Scanner

Description:
    A minimal ARP scanner that discovers devices on the local network and prints
    their IP and MAC addresses. Built with Scapy for quick, readable output.

Usage:
    # Basic scan:
    sudo python3 net_scanner.py -i 192.168.1.0/24

    # Example output:
    Scanning 192.168.1.0/24 ... (run as root if you need)

    --- Device 1 ---
    IP Address:  192.168.1.1
    MAC Address: 00:11:22:33:44:55

Notes:
    - This script must be run with root privileges (sudo) because it sends raw packets.
    - Requires Python 3 and the `scapy` package.
    - Use responsibly — only scan networks you own or have permission to test.

Requirements:
    - Python 3
    - scapy (`pip3 install scapy`)
    - root/sudo
"""

import scapy.all as scapy
import optparse

def get_ip_address():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ipaddress", dest="ip_address", help="Target IP (e.g. 192.168.1.1/24)")

    (options, arguments) = parser.parse_args()

    if not options.ip_address:
        print("Please enter a valid IP, e.g. 192.168.1.0/24")
        exit()
    return options

def scan_network(target_ip):
    arp_request = scapy.ARP(pdst=target_ip)

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast / arp_request
    (answered, unanswered) = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    return answered

def print_answered_devices(answered, target):
    print(f"Scanning {target} ... (run as root if you need)\n")
    if not answered:
        print("No devices found!")
        return

    for index, response in enumerate(answered, start=1):
        received = response[1]
        arp_received = received.getlayer(scapy.ARP)

        responder_ip = arp_received.psrc
        responder_mac = arp_received.hwsrc

        print(f"--- Device {index} ---")
        print(f"IP Address:  {responder_ip}")
        print(f"MAC Address: {responder_mac}\n")

ip_options = get_ip_address()
answered = scan_network(ip_options.ip_address)
print_answered_devices(answered, ip_options.ip_address)