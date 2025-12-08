from hashlib import sha256 as sha
import codecs

#bits -> 16진수 값을 나타내는 바이트 객체 리턴
def decodeBitcoinVal(bits):
	#hex codec 객체 decode_hex를 생성
	decode_hex = codecs.getdecoder('hex_codec')
	binn = decode_hex(bits)[0]
	ret = codecs.encode(binn[::-1], 'hex_codec')
	return ret
	

#Bits 필드값 -> Target 값 변환 함수
def getTarget(bits):
	bits = decodeBitcoinVal(bits)
	bits = int (bits, 16)
	print('Bits = %x' %bits)
	#bits의 첫 1바이트 ‘1a'를 얻어 bit1에 할당
	bit1 = bits >> 4*6
	#bits의 나머지 3바이트 ‘44b9f2'를 base에 할당
	base = bits & 0x00ffffff
	
	sft = (bit1 - 0x3) * 8
	target = base << sft
	print('Target = %x' %target)


#실제 비트코인의 125,552번째 Bits 값
Bits = 'f2b9441a'
getTarget(Bits)
