# 🛡️ Network Packet Sniffer

🚀 A real-time network packet sniffer built using Python and Scapy for monitoring, analyzing, and logging live network traffic.

This project captures packets directly from the network interface, extracts important networking information, and displays it in a structured real-time format.

---

# 📌 Project Overview

The goal of this project was to understand how network traffic flows between systems and how packet analyzers like Wireshark and tcpdump work internally.

The sniffer captures live packets and extracts:

✅ Source IP Address  
✅ Destination IP Address  
✅ Protocol Type  
✅ Source & Destination Ports  
✅ Packet Size  
✅ Live Traffic Statistics  

The project also supports:

🔥 Protocol Filtering  
🔥 JSON Packet Logging  
🔥 Real-Time Packet Monitoring  
🔥 Modular Architecture  
🔥 CLI Arguments  

---

# ⚡ Features

## 🌐 Real-Time Packet Sniffing
Capture packets live from the network interface.

## 📡 Protocol Analysis
Detect and analyze:
- TCP
- UDP
- ICMP

## 🧠 Packet Parsing
Extract:
- Source IP
- Destination IP
- Source Port
- Destination Port
- Packet Size

## 📊 Live Traffic Statistics
Track:
- Total packets
- TCP packets
- UDP packets
- ICMP packets

## 🎯 Protocol Filtering
Filter traffic using:
- `--tcp`
- `--udp`

## 📝 JSON Logging
Save captured packets into:
```text
logs/packets.json
```

## 🏗️ Modular Architecture
Project divided into:
- `main.py`
- `parser.py`
- `filters.py`
- `logger.py`

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core Programming Language |
| Scapy | Packet Capture & Analysis |
| argparse | CLI Argument Parsing |
| JSON | Packet Logging |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
packet-sniffer/
│
├── main.py
├── parser.py
├── filters.py
├── logger.py
├── logs/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

## 📥 Clone Repository

```bash
git clone https://github.com/lakshyatyagi07/packet-sniffer.git
```

---

## 📁 Move Into Project Directory

```bash
cd packet-sniffer
```

---

## 🐍 Create Virtual Environment

```bash
python3 -m venv venv
```

---

## ▶️ Activate Virtual Environment

### Linux / Kali

```bash
source venv/bin/activate
```

### macOS

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install scapy
```

---

# 🚀 Usage

## ▶️ Run Packet Sniffer

```bash
sudo venv/bin/python main.py
```

---

# 🎯 TCP Filter

```bash
sudo venv/bin/python main.py --tcp
```

---

# 🎯 UDP Filter

```bash
sudo venv/bin/python main.py --udp
```

---

# 🖥️ Example Output

```text
[TCP] 192.168.64.3:41838 -> 142.250.71.110:443 | Size: 1294 bytes

Total: 45 | TCP: 31 | UDP: 9 | ICMP: 5
```

---

# 📝 JSON Packet Logging

Captured packets are automatically stored in:

```text
logs/packets.json
```

Each packet log contains:

- Timestamp
- Protocol
- Source IP
- Destination IP
- Source Port
- Destination Port
- Packet Size

---

# 🧠 Learning Outcomes

This project helped in understanding:

✅ TCP/IP Networking  
✅ Packet Structure  
✅ Real-Time Traffic Monitoring  
✅ Network Traffic Analysis  
✅ Python Packet Manipulation  
✅ CLI Utility Development  
✅ JSON Logging Systems  
✅ Modular Software Architecture  
✅ Git & GitHub Workflow  

---

# 🔮 Future Improvements

🚧 IP-Based Filtering  
🚧 Port-Based Filtering  
🚧 Colored Terminal Output  
🚧 Interface Selection  
🚧 Graceful Shutdown Statistics  
🚧 PCAP Export Support  
🚧 Advanced Traffic Analysis  

---

# ⚠️ Disclaimer

This project is developed strictly for educational and learning purposes.

Use packet sniffing tools responsibly and only on networks you own or are authorized to monitor.

---

# 👨‍💻 Author

## Lakshya Tyagi

🔗 GitHub:  
https://github.com/lakshyatyagi07

