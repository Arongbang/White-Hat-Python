from scapy.all import *


def ipSpoof(srcip, dstip):
	ip_packet = IP(src=srcip, dst=dstip)/ICMP()
	
	print(ip_packet.show())
	send(ip_packet)


def main():
	srcip = '172.21.70.227'
	dstip = '172.21.70.180'
	ipSpoof(srcip, dstip)
	
	print('SENT SPOOFED IP [%s] to [%s]' %(srcip, dstip))
	
	
if __name__ == '__main__':
	main()
