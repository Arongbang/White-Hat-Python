from scapy.all import *

#sniff() : 네트워크 패킷을 스니핑하는 함수
#prn : 캡처한 패킷을 처리하기 위한 함수
#count : 패킷을 캡처하는 횟수
sniff(prn=lambda x: print(x), count=1)
