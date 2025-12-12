#UDP를 이용하여 서브네트워크의 모든 잠재적 호스트로 메시지 전송하는 코드

from socket import *
from netaddr import IPNetwork, IPAddress

def sendMsg(subnet, msg):
	#UDP 소켓 생성
	#UDP는 TCP와 달리 원격 호스트와 연결된 소켓이 아니므로, 목적지 IP는 데이터를 보낼 시점에 지정
	sock = socket(AF_INET, SOCK_DGRAM)
	#IPNetwork(subnet) : 서브네트워크의 모든 IP주소를 담고 있음
	for ip in IPNetwork(subnet):
		try:
			print('SENDING MESSAGE to [%s]' %ip)
			#sendto()에 유니코드로 메시지 전달하면 오류 발생
			#sendto() : 서브네트워크의 모든 IP에 대해 9000번 포트로 메시지 전송
			sock.sendto(msg.encode('utf-8'), ('%s' %ip, 9000))
		except Exception as e:
			print(e)


def main():
	host = gethostbyname(gethostname())
	#IP주소가 ’192.168.0.5‘인 경우, 서브네트워크는 ‘192.169.0.5/24’로 표현하면 됨
	subnet = host + '/24'
	msg = 'KNOCK!KNOCK!'
	sendMsg(subnet, msg)
	

if __name__ == '__main__':
	main()
