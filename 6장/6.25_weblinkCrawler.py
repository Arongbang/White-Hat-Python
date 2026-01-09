#웹 링크 크롤러

from urllib.request import urlopen, Request
import re
import sys

user_agent = 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
href_links = []

#getLinks() : doc 내 모든 'href' 태그를 찾아 링크 정보 얻는 함수
#doc : HTML 페이지 내용
#parent : 상위 url 주소
def getLinks(doc, home, parent):
	global href_links
	href_pattern = [r'href="([^"]+)"', r'href=([^\s>]+)', r"href='([^']+)'"]
	tmp_urls = []
	
	for n in range(len(href_pattern)):
		#re.I : 대소문자 구분 X
		tmp_urls += re.findall(href_pattern[n], doc, re.I)
	
	for url in tmp_urls:
		url = url.strip()
		url = url.replace('\'', '"')
		#맨 마지막이 공백 || 쌍따옴표가 없음
		if url.endswith(' ') or '"' not in url:
			url = url.split('=')[1]
		else:
			url = url.split('"')[1]
		
		if len(url) is 0:
			continue
		
		if url.find('http://') is -1:
			if url[0] == '/':
				url = home + url
			#앞의 2글자가 ./ 일때
			elif url[:2] == './':
				url = 'http://' + parent + url[1:]
			else:
				url = 'http://' + parent + '/' + url
		
		if url in href_links:
			continue
		
		if '.html' not in url:
			href_links.append(url)
			continue
		
		runCrawler(home, url)
	
#url로 접속 후 HTML 페이지를 읽어 와서 리턴
def readHtml(url):
	try:
		req = Request(url)
		req.add_header('User-Agent', user_agent)
		with urlopen(req) as h:
			doc = h.read()
	
	except Exception as e:
		print('ERROR: %s' %url)
		print(e)
		return None
		
	return doc.decode()

def runCrawler(home, url):
	global href_links
	href_links.append(url)
	print('GETTING ALL LINKS in [%s]' %url)
	
	try:
		#페이지 득
		doc = readHtml(url)
		if doc is None:
			return
		
		tmp = url.split('/')
		#도메인이랑 중간경로만 뽑음
		parent = '/'.join(tmp[2:-1])
		
		#페이지에서 링크 정보 추출
		if parent:
			getLinks(doc, home, parent)
		else:
			getLinks(doc, home, home)
	except KeyboardInterrupt:
		print('Terminated by USER..Saving Crawled Links')
		finalize()
		#프로그램 종료
		sys.exit(0)
	return

#링크 정보를 파일로 저장
def finalize():
	with open('crawled_links.txt', 'w+') as f:
		for href_link in href_links:
			f.write(href_link + '\n')
	
	print('+++ CRAWLED TOTAL href_links: [%s]' %len(href_links))


def main():
	targeturl = 'http://localhost/DVWA'
	home = 'http://' + targeturl.split('/')[2]
	print('+++ WEB LINK CRAWLER START > [%s]' %targeturl)
	runCrawler(home, targeturl)
	finalize()
	

main()
