# Network Scanner

A simple Python script to scan your local network using ARP requests.  
It discovers devices connected to the network and prints their IP and MAC addresses in a clean, readable format.

---

## Features

- 🔍 Discover devices in the local network  
- 🌐 Show IP and MAC addresses of active hosts  
- ⚡ Lightweight and fast (uses ARP requests)  

---

## Usage

### Basic scan

```bash
sudo python3 net_scanner.py -i 192.168.1.0/24
```

### Show help menu

```bash
python3 net_scanner.py --help
```

---

## Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| -i, --ipaddress | Target IP | 192.168.1.0/24 |

---

## Example Output

```text
Scanning 192.168.1.0/24 ... (run as root if you need)

--- Device 1 ---
IP Address:  192.168.1.1
MAC Address: 00:11:22:33:44:55

--- Device 2 ---
IP Address:  192.168.1.100
MAC Address: 00:aa:66:77:88:99
```

---

## Requirements

- 🐧 Linux OS  
- 🐍 Python 3  
- 📦 scapy (`pip3 install scapy`)  
- ⚡ Root/sudo privileges  

---

## Notes

- ❗ Root privileges are required to run the script  
- 📡 Works on local networks only (LAN)  
- ⚠️ Do not scan networks you don’t own or don’t have permission to test  


---

**Important:** Use responsibly and only on networks you own or have explicit permission to scan. Unauthorized scanning may be illegal.
