# pyright: reportUndefinedVariable=false

import sys
from scapy.all import *
import network_tools
import storage


def main():
    output_packet_details = []

    sniff(count= 3, prn=lambda p:network_tools.analysePacket(p, output_packet_details))

    network_tools.printPacketDetailsInline(output_packet_details)
    network_tools.printFullPacketDetails(output_packet_details)
    
    storage.db_init()

    storage.insertPacketDetails(output_packet_details)


if __name__ ==  "__main__":
    main()