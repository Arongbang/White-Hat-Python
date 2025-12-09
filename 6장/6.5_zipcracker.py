#파일이름이 'locked.zip'인 패스워드로 보호된 ZIP 압축파일을 사전 공격으로 압축해제 & 패스워드 추출하는 코드

#ZIP 파일 관련 다양한 메소드를 제공
import zipfile
from threading import Thread

def crackzip(zfile, passwd):
	try:
		#passwd를 패스워드로 하여 zfile의 모든 내용에 대해 압축 해제를 시도
		zfile.extractall(path='./locked', pwd=passwd)
		print('ZIP file extracted successfully! PASS=[%s]' %passwd.decode())
		return True
	
	except:
		pass
	return False



def main():
	dictfile = 'dictionary.txt'
	zipfilename = 'locked.zip'
	#일반파일은 open()을 이용하여 얻은 파일핸들러로 파일을 다룸
	#ZIP파일은 ZipFile 객체를 생성하여 ZIP파일을 다룸
	zfile = zipfile.ZipFile(zipfilename, 'r')
	pfile = open(dictfile, 'r')
	
	for line in pfile.readlines():
		#crackzip() 함수를 스레드로 호출
		passwd = line.strip('\n')
		#스레드 : 하나의 프로세스 안에 있는 또 다른 작은 프로세스
		#스레드로 호출하는 이유 : crackzip()이 연산하는 동안 for구문을 계속 수행하기 위함
		t = Thread(target=crackzip, args=(zfile, passwd.encode('utf-8')))
		t.start()
	

main()
