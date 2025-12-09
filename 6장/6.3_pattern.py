#문장p의 패턴을 표준화한 결과 리턴
def makePattern(p):
	#문자에 부여한 번호를 임시로 저장하기 위한 사전 자료
	tmp = {}
	#패턴 결과를 담을 리스트 자료
	res = []
	#문자에 부여할 번호
	index = 0
	for c in p:
		if c in tmp:
			res.append(tmp[c])
		else:
			tmp[c] = str(index)
			res.append(str(index))
			index += 1
	return ';'.join(res)
	

#msg에서 1자씩 이동하면서 p와 동일한 패턴을 스캔 & 동일부분 찾으면 리턴
def findPattern(msg, p):
	pattern = makePattern(p)
	blocksize = len(p)
	pos = 0
	while True:
		data = msg[pos:pos + blocksize]
		if len(data) < blocksize:
			break
		
		ptrn = makePattern(data)
		if ptrn == pattern:
			return data
			break
		pos += 1


if __name__ == '__main__':
	#암호 문장
	msg = """53%%#305))6*;4826)4%=')4%);806;48#8@60'))85;1%(;;-%*8#83(88)5*#;46(;88*96*?;8)*%(;485); 5*#2:*%(;4956*2(5*c4)8@8*;4069285);)6#8)4%%;1(%9;48081;8:8%1;48#85;4')-485#528806*81(%9;48;(88;4(%?34;484%;161;:188;%?;"""
	
	known_plaintext = ['goodglass', 'mainbranch']
	for p in known_plaintext:
		ret = findPattern(msg, p)
		print('[%s] = [%s]' %(p, ret))
