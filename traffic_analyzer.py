import pcapy
from scapy.all import *
import matplotlib.pyplot as plt
from scapy.layers.l2 import Ether


# Network interface to capture packets from
interface = "en0"

# Capture duration in seconds
capture_duration = 2

# Function to process captured packets
def process_packet(header, data):
    try:
        packet_scapy = Ether(data)
        protocol = packet_scapy.getlayer(2).name
        protocol_counts[protocol] += 1
        total_bytes[protocol] += len(data)
    except Exception as e:
        print(f"Error processing packet: {e}")  # Print any errors encountered

# Initialize dictionaries to store protocol counts and total bytes
protocol_counts = defaultdict(int)
total_bytes = defaultdict(int)

# Capture packets
print(f"Capturing packets on interface {interface} for {capture_duration} seconds...")
cap = pcapy.open_live(interface, 65536, 1, 0)
cap.loop(capture_duration, process_packet)

# Visualize results
protocols = list(protocol_counts.keys())
counts = list(protocol_counts.values())
bytes_transferred = list(total_bytes.values())

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(protocols, counts)
plt.title("Packets per Protocol")
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")

plt.subplot(1, 2, 2)
plt.bar(protocols, bytes_transferred)
plt.title("Total Bytes Transferred per Protocol")
plt.xlabel("Protocol")
plt.ylabel("Total Bytes")

plt.tight_layout()
plt.show()