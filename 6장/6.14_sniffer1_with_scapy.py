from scapy.all import *

def showPacket(packet):
	print(packet.show())


def main(filter):
	#sniff() : 네트워크 패킷을 스니핑하는 함수
	#filter : 원하는 패킷만 볼 수 있는 필터를 지정
	#prn : 캡처한 패킷을 처리하기 위한 함수
	#count : 패킷을 캡처하는 횟수
	
	#sniff()가 showPacket() 호출할 때 캡처한 패킷을 자동으로 넘김
	sniff(filter=filter, prn=showPacket, count=1)
	

if __name__ == '__main__':
	filter = 'ip'
	main(filter)
