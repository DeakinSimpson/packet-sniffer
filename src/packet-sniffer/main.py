# pyright: reportUndefinedVariable=false

import sys
from scapy.all import *

def analysePacket(pkt: packet, output_packet_details):
    output_packet_details.append({
        "time": pkt.time,
        "src": pkt[IP].src,
        "dst": pkt[IP].dst,
        "proto":pkt[IP].proto,
        # if packet is TCP
        "sport": pkt[TCP].sport if pkt.haslayer(TCP) else None,
        "dport": pkt[TCP].dport if pkt.haslayer(TCP) else None,
        "size": len(pkt),
        # if packet is DNS packet
        "dns-query": pkt[DNS].qd.qname.decode() if pkt.haslayer(DNS) and packet[DNS].qd else None,
        # append the raw data (could be used later)
        "raw": raw(pkt),
    })


def main():
    output_packet_details = []

    sniff(count= 1, prn=lambda p:analysePacket(p, output_packet_details))

    print(output_packet_details[0]['raw'])
    

if __name__ ==  "__main__":
    main()