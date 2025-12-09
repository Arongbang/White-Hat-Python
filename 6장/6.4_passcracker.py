#사전을 이용한 유닉스 패스워드 크래킹 코드
import ccrypt512 as crypt

def findPass(passhash, dictfile):
	#passhash의 3~10번째 문자가 salt
	salt = passhash[3:11]
	with open(dictfile, 'r') as dfile:
		for word in dfile.readlines():
			word = word.strip('\n')
			cryptwd = crypt.sha512_crypt(word, salt)
			if cryptwd == passhash:
				return word
	return ''	


def main():
	dictfile = 'dictionary.txt'
	#with open() as : 수행 코드가 종료되면 자동으로 파일 닫음 & file.close() 같은 거 사용 안해도 됨
	with open('passwords.txt', 'r') as passFile:
		for line in passFile.readlines():
			data = line.split(':')
			#strip() : 공백 제거
			user = data[0].strip()
			passwd = data[1].strip()
			word = findPass(passwd, dictfile)
			if word:
				print('FOUND Password: ID [%s] Password [%s]' %(user, word))
			else:
				print('Password Not Found!')
	


main()
