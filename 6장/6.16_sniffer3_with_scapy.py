#'user'나 ‘pass'라는 단어가 있을 경우, 서버 IP와 TCP 메시지를 화면에 출력
from scapy.all import *


def showPacket(packet):
	data = '%s' %(packet[TCP].payload)
	
	if 'user' in data.lower() or 'data' in data.lower():
		print('+++[%s] : %s' %(packet[IP].dst, data))
	
			
def main(filter):
	sniff(filter=filter, prn=showPacket, count=0, store=0)
	

if __name__ == '__main__':
	#프로토콜이 TCT이며 포트는25, 110, 143만 스니핑하도록 filter 인자 전달
	filter = 'tcp port 25 or tcp port 110 or port 143'
	main(filter)
