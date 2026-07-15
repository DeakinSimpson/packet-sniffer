# pyright: reportUndefinedVariable=false

import sys
from scapy.all import *
from datetime import datetime

# this function converts the sniffed packets into a list of dict's that contain packet info
def analysePacket(pkt: packet, output_packet_details):
    output_packet_details.append({
        "time": pkt.time,
        "src": pkt[IP].src,
        "dst": pkt[IP].dst,
        "proto":pkt[IP].proto,
        "ttl": pkt[IP].ttl,
        # if packet is TCP
        "sport": pkt[TCP].sport if pkt.haslayer(TCP) else None,
        "dport": pkt[TCP].dport if pkt.haslayer(TCP) else None,
        "size": len(pkt),
        # if packet is DNS packet
        "dns-query": pkt[DNS].qd.qname.decode() if pkt.haslayer(DNS) and packet[DNS].qd else None,
        # append the raw data (could be used later)
        "raw": raw(pkt),
    })

# this will print the details of each packet
def printPacketDetailsInline(packets):
    for pkt in packets:
        print(f'Time: {datetime.fromtimestamp(pkt['time'])}, src IP: {pkt['src']}, dst IP: {pkt['dst']}, Protocol: {pkt['proto']}, ttl: {pkt['ttl']}, sport: {pkt['sport']}, dport: {pkt['dport']}, size: {pkt['size']}, dns-query: {pkt['dns-query']}')

def main():
    output_packet_details = []

    sniff(count= 10, prn=lambda p:analysePacket(p, output_packet_details))

    printPacketDetailsInline(output_packet_details)
    

if __name__ ==  "__main__":
    main()