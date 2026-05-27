from scapy.all import sniff
from parser import parse_packet
from logger import save_to_json
from filters import should_filter

from datetime import datetime
import argparse

total_packets = 0
tcp_count = 0
udp_count = 0
icmp_count = 0

parser = argparse.ArgumentParser()

parser.add_argument("--tcp", action="store_true")
parser.add_argument("--udp", action="store_true")

args = parser.parse_args()

def packet_callback(packet):

    global total_packets
    global tcp_count
    global udp_count
    global icmp_count

    parsed_packet = parse_packet(packet)

    if not parsed_packet:
        return

    protocol_name = parsed_packet["protocol"]

    if should_filter(protocol_name, args):
        return

    total_packets += 1

    if protocol_name == "TCP":
        tcp_count += 1

    elif protocol_name == "UDP":
        udp_count += 1

    elif protocol_name == "ICMP":
        icmp_count += 1

    packet_data = {

        "timestamp": str(datetime.now()),
        **parsed_packet
    }

    save_to_json(packet_data)

    print(
        f"[{protocol_name}] "
        f"{parsed_packet['source_ip']}:{parsed_packet['source_port']} -> "
        f"{parsed_packet['destination_ip']}:{parsed_packet['destination_port']} | "
        f"Size: {parsed_packet['packet_size']} bytes"
    )

    print(
        f"Total: {total_packets} | "
        f"TCP: {tcp_count} | "
        f"UDP: {udp_count} | "
        f"ICMP: {icmp_count}"
    )

    print("-" * 60)

print("=" * 60)
print("NETWORK PACKET SNIFFER STARTED")
print("=" * 60)

sniff(prn=packet_callback)