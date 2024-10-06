# NTAT
This proof of concept demonstrates the core functionalities of the network traffic analysis tool by capturing network packets, dissecting them using Wireshark, and visualizing basic traffic statistics.
# Code Overview:

The repository contains a Python script that performs the following actions:

Capture packets: Uses the pcapy library to capture network packets from a specified interface.
Dissect packets: Utilizes the scapy library (which provides a Python wrapper for libwireshark) to dissect the captured packets and extract relevant information (e.g., source/destination IP addresses, protocols, packet size).
Calculate statistics: Aggregates basic statistics like the number of packets per protocol and the total bytes transferred.
Visualize data: Uses matplotlib to create a simple bar chart showing the distribution of traffic by protocol.

# Instructions to Compile and Run:

Operating System: Ubuntu 22.04 LTS
Python Version: Python 3.10
Required Libraries: pcapy, scapy, matplotlib