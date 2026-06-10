from scapy.all import sniff, IP

# Function to process packets
def packet_callback(packet):
    if packet.haslayer(IP):
        print("\n--- Packet Captured ---")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

        if packet.payload:
            print("Payload:", packet.payload)

# Start sniffing packets
print("Starting Packet Analyzer...")
print("Press Ctrl + C to stop.\n")

sniff(prn=packet_callback, count=5)