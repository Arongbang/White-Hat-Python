#ctrl + c 누를 때까지 패킷을 지속적으로 스니핑 & 스니핑한 패킷에서 IP헤더 부분만 출력

from socket import *
#코드가 구동되는 컴퓨터의 OS 종류를 확인하기 위해
import os

def recvData(sock):
	data = ''
	try:
		data = sock.recvfrom(65565)
	except timeout:
		data = ''
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
	
	count = 1
	try:
		while True:
			data = recvData(sniffer)
			print('SNIFFED [%d] %s' %(count, data[:20]))
			count += 1
			
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
