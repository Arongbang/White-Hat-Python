#이 코드가 실행되는 컴퓨터에 송수신되는 패킷 하나를 가로채서 그 내용을 화면에 출력하는 코드

from socket import *
#코드가 구동되는 컴퓨터의 OS 종류를 확인하기 위해
import os

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
	sniffer.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
	
	#윈도우인 경우
	if os.name == 'nt':
		sniffer.ioctl(SIO_RCVALL, RCVALL_ON)
	packet = sniffer.recvfrom(65565)
	print(packet)
	
	#윈도우인 경우
	if os.name == 'nt':
		sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)
	
	
def main():
	host = gethostbyname(gethostname())
	print('START SNIFFING at [%s]' %host)
	sniffing(host)


if __name__ == '__main__':
	main()
