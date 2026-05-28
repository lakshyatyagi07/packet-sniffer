from scapy.all import sniff
from parser import parse_packet
from logger import save_to_json
from filters import should_filter

from datetime import datetime
from rich import print

import argparse
import signal
import sys

total_packets = 0
tcp_count = 0
udp_count = 0
icmp_count = 0

parser = argparse.ArgumentParser()

parser.add_argument("--tcp", action="store_true")
parser.add_argument("--udp", action="store_true")

parser.add_argument("--ip", type=str)
parser.add_argument("--port", type=int)

args = parser.parse_args()

def shutdown_handler(signum, frame):

    print("\n")
    print("[bold red]" + "=" * 50 + "[/bold red]")
    print("[bold red]FINAL STATISTICS[/bold red]")
    print("[bold red]" + "=" * 50 + "[/bold red]")

    print(f"[cyan]Total Packets :[/cyan] {total_packets}")
    print(f"[green]TCP Packets   :[/green] {tcp_count}")
    print(f"[yellow]UDP Packets  :[/yellow] {udp_count}")
    print(f"[magenta]ICMP Packets :[/magenta] {icmp_count}")

    print("[bold red]" + "=" * 50 + "[/bold red]")
    print("[bold red]Sniffer stopped successfully.[/bold red]")

    sys.exit(0)

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

    if args.ip:

        if (
            parsed_packet["source_ip"] != args.ip
            and parsed_packet["destination_ip"] != args.ip
        ):
            return

    if args.port:

        if (
            parsed_packet["source_port"] != args.port
            and parsed_packet["destination_port"] != args.port
        ):
            return

    total_packets += 1

    if protocol_name == "TCP":
        tcp_count += 1
        color = "green"

    elif protocol_name == "UDP":
        udp_count += 1
        color = "yellow"

    elif protocol_name == "ICMP":
        icmp_count += 1
        color = "magenta"

    else:
        color = "white"

    packet_data = {

        "timestamp": str(datetime.now()),
        **parsed_packet
    }

    save_to_json(packet_data)

    print(
        f"[bold {color}][{protocol_name}][/bold {color}] "
        f"{parsed_packet['source_ip']}:{parsed_packet['source_port']} -> "
        f"{parsed_packet['destination_ip']}:{parsed_packet['destination_port']} | "
        f"Size: {parsed_packet['packet_size']} bytes"
    )

    print(
        f"[cyan]Total:[/cyan] {total_packets} | "
        f"[green]TCP:[/green] {tcp_count} | "
        f"[yellow]UDP:[/yellow] {udp_count} | "
        f"[magenta]ICMP:[/magenta] {icmp_count}"
    )

    print("[blue]" + "-" * 60 + "[/blue]")

print("[bold cyan]" + "=" * 60 + "[/bold cyan]")
print("[bold green]NETWORK PACKET SNIFFER STARTED[/bold green]")
print("[bold cyan]" + "=" * 60 + "[/bold cyan]")

signal.signal(signal.SIGINT, shutdown_handler)

sniff(prn=packet_callback)