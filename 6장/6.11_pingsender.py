import os
from netaddr import IPNetwork, IPAddress
from socket import *
from threading import Thread

#시스템의 ping 명령을 직접 호출하여 해당 IP로 ping을 1회 전송하는 함수
def sendPing(ip):
	try:
		ret = os.system('ping -n 1 %s' %ip)
	except Exception as e:
		print(e)
	
def main():
	host = gethostbyname(gethostname())
	subnet = host + '/24'
	for ip in IPNetwork(subnet):
		t = Thread(target=sendPing(), args=(ip,))
		t.start()
	
	
if __name__ == '__main__':
	main()
