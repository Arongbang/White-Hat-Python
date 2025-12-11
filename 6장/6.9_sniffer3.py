#ctrl + c 누를 때까지 패킷을 지속적으로 스니핑 & 스니핑한 패킷에서 IP헤더 부분만 출력

from socket import *
#코드가 구동되는 컴퓨터의 OS 종류를 확인하기 위해
import os
#바이너리 데이터를 파이썬의 자료형으로 변환위해
import struct

def parse_ipheader(data):
	ipheader = struct.unpack('!BBHHHBBH4s4s', data[:20])
	return ipheader
	

def getProtocol(ipheader):
	protocols = {1:'ICMP', 6: 'TCP', 17: 'UDP'}
	proto = ipheader[6]
	if proto in protocols:
		return protocols[proto]
	else:
		return 'OTHERS'

def getIP(ipheader):
	#inet_ntoa() : 바이트 문자열로 된 IP를 IP 주소 형식으로 변환
	src_ip = inet_ntoa(ipheader[8])
	dest_ip = inet_ntoa(ipheader[9])
	return (src_ip, dest_ip)

def getIPHeaderLen(ipheader):
	#0x0F가 ‘0000 1111’이므로 비트 AND 연산자하면 뒤의 4비트의 정보만 나옴
	ipheaderlen = ipheader[0] & 0x0F
	#해당값의 단위가 4바이트라서 4 곱함
	ipheaderlen *= 4
	return ipheaderlen
	
def getTypeCode(icmp):
	icmpheader = struct.unpack('!BB', icmp[:2])
	icmp_type = icmpheader[0]
	icmp_code = icmpheader[1]
	return (icmp_type, icmp_code)

def recvData(sock):
	data = ''
	try:
		data = sock.recvfrom(65565)
	except timeout:
		data = ''
	#첫번째 멤버인 바이트코드에 IP 헤더가 포함되어 있기 때문에 data[0]을 리턴
	return data[0]


def sniffing(host):
	#윈도우인 경우
	if os.name == 'nt':
		#sock_protocol : 소켓을 생성할 때 프로토콜을 지정하는 세 번째 인자
		sock_protocol = IPPROTO_IP
	else:
		#윈도우는 프로토콜에 관계없이 들어오는 모든 패킷을 가로채기 때문에 IP를 지정해도 무관 
		#유닉스나 리눅스는 ICMP를가로채겠다는 걸 명시해야 함
		sock_protocol = IPPROTO_ICMP
		
	sniffer = socket(AF_INET, SOCK_RAW, sock_protocol)
	sniffer.bind((host, 0))
	#setsockopt() : 가로채는 패킷에 IP 헤더를포함하라고 소켓의 옵션으로 지정
	sniffer.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
	
	#윈도우인 경우
	if os.name == 'nt':
		sniffer.ioctl(SIO_RCVALL, RCVALL_ON)
	
	try:
		while True:
			data = recvData(sniffer)
			ipheader = parse_ipheader(data[:20])
			ipheaderlen = getIPHeaderLen(ipheader)
			protocol = getProtocol(ipheader)
			src_ip, dest_ip = getIP(ipheader)
			if protocol == 'ICMP':
				offset = ipheaderlen
				icmp_type, icmp_code = getTypeCode(data[offset:])
				print('%s -> %s: ICMP: Type [%d], Code [%d]' %(src_ip, dest_ip, icmp_type, icmp_code))
	except KeyboardInterrupt:
		if os.name == 'nt':
			sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)


def main():
	#gethostbyname() : 호스트 이름을 IPv4 형식으로 변경
	#gethostname() : 현재 호스트의 이름을 리턴
	host = gethostbyname(gethostname())
	print('START SNIFFING at [%s]' %host)
	sniffing(host)


if __name__ == '__main__':
	main()
