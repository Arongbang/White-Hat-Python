#개선된 화면 캡쳐 코드(2개의 모니터인 경우에도 캡처)

import win32gui, win32api, win32ui, win32con

def getScreenshot():
	hwnd = win32gui.GetDesktopWindow()
	
	width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
	height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
	left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
	top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
	
	#데스크탑 전체 윈도우에 대한 디바이스 컨텍스트
	#Device Context : 출력에 필요한 모든 정보를 가진 Windows 데이터 구조체
	hDC = win32gui.GetWindowDC(hwnd)
	#파이썬에서 사용가능하도록 핸들로 변환
	pDC = win32ui.CreateDCFromHandle(hDC)
	#지정된 디바이스 컨텍스트에 호환되는 메모리 디바이스 컨텍스트 생성
	#메모리 DC : 화면이 아니라 RAM에 있는 비트맵에 그림을 그림
	memDC = pDC.CreateCompatibleDC()
	
	#비트맵 객체 screenshot을 생성
	screenshot = win32ui.CreateBitmap()
	#pDC와 호환되는 전체화면 크기로 구성
	screenshot.CreateCompatibleBitmap(pDC, width, height)
	#비트맵 객체 screenshot을 memDC에 지정
	memDC.SelectObject(screenshot)
	
	#컬러 데이터를 memDC에 비트 블록 단위로 전송
	memDC.BitBlt((0,0), (width, height), pDC, (left, top), win32con.SRCCOPY)
	screenshot.SaveBitmapFile(memDC, 'c:/6.31_screenshot.bmp')
	
	#memDC & screenshot 객체 제거
	memDC.DeleteDC()
	win32gui.DeleteObject(screenshot.GetHandle())


def main():
	getScreenshot()


if __name__ == '__main__':
	main()
