# pyright: reportUndefinedVariable=false

import sys
from scapy.all import *
import network_sniffer


def main():
    output_packet_details = []

    sniff(count= 3, prn=lambda p:network_sniffer.analysePacket(p, output_packet_details))

    network_sniffer.printPacketDetailsInline(output_packet_details)
    network_sniffer.printFullPacketDetails(output_packet_details)
    

if __name__ ==  "__main__":
    main()