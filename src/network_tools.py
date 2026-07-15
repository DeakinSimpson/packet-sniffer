# pyright: reportUndefinedVariable=false

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
        "dns_query": pkt[DNS].qd.qname.decode() if pkt.haslayer(DNS) and packet[DNS].qd else None,
        # append the raw data (could be used later)
        "raw": raw(pkt),
    })

# this will print the details of each packet
def printPacketDetailsInline(packets):
    for pkt in packets:
        print(f'Time: {datetime.fromtimestamp(pkt['time'])}, src IP: {pkt['src']}, dst IP: {pkt['dst']}, Protocol: {pkt['proto']}, ttl: {pkt['ttl']}, sport: {pkt['sport']}, dport: {pkt['dport']}, size: {pkt['size']}, dns_query: {pkt['dns_query']}')

# prints the full packet details of each packer
def printFullPacketDetails(packets, print_raw=False):
    i = 0

    for pkt in packets:
        print(f'--------------------packet {i}--------------------')
        print(f'Time: {datetime.fromtimestamp(pkt['time'])}')
        print(f'src IP: {pkt['src']}')
        print(f'dst IP: {pkt['dst']}')
        print(f'Protocol: {pkt['proto']}')
        print(f'ttl: {pkt['ttl']}')
        print(f'sport: {pkt['sport']}')
        print(f'dport: {pkt['dport']}')
        print(f'size: {pkt['size']}')
        print(f'dns_query: {pkt['dns_query']}')
        if print_raw: print(f'raw: {pkt['raw']}')
        print(f'------------------------------------------------\n')

        i += 1