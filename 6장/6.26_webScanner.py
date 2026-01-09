#웹 스캐너

from urllib.request import urlopen, Request, URLError, qouote
from queue import Queue
from threading import Thread

user_agent = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firerfox/2.0.0.11'

def webScanner(q, targethost, exts):
	while not q.empty():
		#scanlist : 접속할 URI를 담기 위한 리스트 자료
		scanlist = []
		toscan = q.get()
		
		if '.' in toscan: #FILE
			scanlist.append('%s' %toscan)
			for ext in exts:
				scanlist.append('%s%s' %(toscan, ext))
		else: #DIR
			scanlist.append('%s/' %toscan)
		
		for toscan in scanlist:
			#quote() : URL에 사용되는 '문자열'로 인코딩
			url = '%s/%s' %(targethost, quote(toscan))
			
			try:
				req = Request(url)
				req.add_header('User-Agent', user_agent)
				res = urlopen(req)
				if len(res.read()):
					print('[%d]:%s' %(res.code, url))
				res.close()
			except URLError as e:
				pass


def main():
	targethost = 'http://172.21.70.227'
	wordlist = './all.txt'
	#추가적으로 더 찾을 확장자
	exts = ['~', '~1', '.back', '.bak', '.old', '.org', '_backup']
	q = Queue()
	
	with open(wordlist, 'rt') as f:
		#readlines() 리스트로 리턴하므로 	words는 리스트 자료
		words = f.readlines()
	
	for word in words:
		word = word.rstrip()
		q.put(word)
	
	print('+++ [%s] SCANning START..' %targethost)
	
	for i in range(50):
		t = Thread(target=webScanner, args=(q, targethost, exts))
		t.start()


if __name__ == '__main__':
	main()
