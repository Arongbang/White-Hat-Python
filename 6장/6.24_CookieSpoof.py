#쿠키 정보 조작하여 요청하기
from urllib.request import urlopen, Request

user_agent = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firerfox/2.0.0.11'
#조작하려는 쿠키 문자열
cookie = 'NID=1234; expires=Thu, 25-Aug-2016 06:26:36 GMT; path=/; domain=.google.co.kr; HttpOnly'

def cookieSpoof(url):
	req = Request(url)
	req.add_header('User-Agent', user_agent)
	req.add_header('Cookie', cookie)
	
	with urlopen as h:
		print(h.read().decode('utf-8'))
	
	
def main():
	url = 'http://www.google.com'
	cookieSpoof(url)
	

if __name__ == '__main__':
	main()
