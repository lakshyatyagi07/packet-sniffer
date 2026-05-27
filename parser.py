from scapy.all import IP, TCP, UDP

def get_protocol_name(protocol_number):

    if protocol_number == 1:
        return "ICMP"

    elif protocol_number == 6:
        return "TCP"

    elif protocol_number == 17:
        return "UDP"

    else:
        return "OTHER"

def parse_packet(packet):

    if not packet.haslayer(IP):
        return None

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    protocol_number = packet[IP].proto
    protocol_name = get_protocol_name(protocol_number)

    packet_size = len(packet)

    source_port = "N/A"
    destination_port = "N/A"

    if packet.haslayer(TCP):

        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif packet.haslayer(UDP):

        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    return {

        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "protocol": protocol_name,
        "source_port": source_port,
        "destination_port": destination_port,
        "packet_size": packet_size
    }