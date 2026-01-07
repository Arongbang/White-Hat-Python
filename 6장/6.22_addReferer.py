#HTTP 요청 메시지에 Referer 헤더를추가하여 목적지 URL로 연결
from urllib.request import Request, urlopen

def addReferer(url):
	#Request() : URL 요청을 추상화한 클래스 & URL로 요청 헤더를 구성하여 전송할 수 있도록 함
	req = Request(url)
	req.add_header('Referer', 'http://www.mysite.com')
	
	#urlopen() : HTTP GET 요청 메시지를 생성 후 목적지 URL로 요청
	#urlopen(url, data=데이터) 와 같이 data를 지정하면 HTTP POST 요청메시지 생성 및 목적지 URL로 요청
	#서버 요청에 대한 응답을 응답 객체(http.client.HTTPResponse) h로 받아서 처리
	with urlopen(req) as h:
		#서버가 보내준 응답 body를 “바이트(bytes)”로 읽음
		print(h.read().decode('utf-8'))
	

def main():
	#요청 HTTP 헤더를 리턴
	url = 'http://httpbin.org/headers'
	addReferer(url)


if __name__ == '__main__':
	main()
