from pywinauto.application import Application
import pywinauto
 
# 열려진 다이얼로그 창에 연결 합니다.
app = pywinauto.application.Application()
app.Connect(title="업로드할 파일 선택") 
 
# 다이얼로그 창을 정의 합니다.
mainWindow = app['업로드할 파일 선택'] # main windows' title
 
# 파일 이름 입력하는 창에가서 'test.txt' 라고 입력합니다.
ctrl=mainWindow['Edit'] 
mainWindow.SetFocus()
ctrl.ClickInput()
ctrl.TypeKeys("test.txt")
 
# 열기 버튼을 클릭합니다.
mainWindow.Button1.click()
