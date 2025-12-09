from time import sleep
from threading import Thread

answer = 0

def longtime_job(a,b):
	#전역 변수를 사용한다는 의미
	global answer
	print('++JOB START\n')
	sleep(5)
	answer = a*b
	print('++JOB RERSULT [%d]' %answer)
	
	
def main():
	a, b = 3, 4
	#longtime_job(a, b)
	t = Thread(target=longtime_job, args=(a,b))
	t.start()
	print('**RUN MAIN LOGIC')
	tmp = a + b
	#스레드 t가 종료할 때까지 기다림
	t.join()
	final = answer + tmp
	print('FINAL RESULT [%d]' %final)
	

if __name__ == '__main__':
	main()
