#UDP를 이용하여 서브네트워크의 모든 잠재적 호스트로 메시지 전송하는 코드

from socket import *
from netaddr import IPNetwork, IPAddress

def sendMsg(subnet, msg):
	#UDP 소켓 생성
	sock = socket(AF_INET, SOCK_DGRAM)
	for ip in IPNetwork(subnet):
		try:
			print('SENDING MESSAGE to [%s]' %ip)
			sock.sendto(msg.encode('utf-8'), ('%s' %ip, 9000))
		except Exception as e:
			print(e)


def main():
	host = gethostbyname(gethostname())
	subnet = host + '/24'
	msg = 'KNOCK!KNOCK!'
	sendMsg(subnet, msg)
	

if __name__ == '__main__':
	main()
