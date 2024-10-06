from scapy.all import sniff, IP, TCP, UDP

# Function to process captured packets
def process_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src  # Source IP
        ip_dst = packet[IP].dst  # Destination IP

        # Check if it's a TCP or UDP packet
        if packet.haslayer(TCP):
            protocol = "TCP"
            sport = packet[TCP].sport  # Source port
            dport = packet[TCP].dport  # Destination port
        elif packet.haslayer(UDP):
            protocol = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        else:
            protocol = "Other"
            sport = None
            dport = None

        print(f"Packet: {protocol} {ip_src}:{sport} --> {ip_dst}:{dport}")

# Start sniffing packets
print("Sniffing started... Press Ctrl+C to stop.")
sniff(prn=process_packet, count=10)
