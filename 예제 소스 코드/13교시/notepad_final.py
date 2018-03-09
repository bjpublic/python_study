from pywinauto.application import Application
 
# 메모장를 띄웁니다.
app = Application().start("notepad.exe")
 
# 메모장에 code를 적습니다.
app.UntitledNotepad.Edit.type_keys("print {(}'test'{)}", with_spaces = True)
 
# "파일' > 저장" 메뉴를 실행 합니다.
app.UntitledNotepad.menu_select("파일(&F)->저장(&S)")
 
# '다른 이름으로 저장' 창의 속성을 리스트업 합니다.
# app.다른_이름으로_저장.print_control_identifiers()
 
# 파일 전체 경로를 입력 합니다.
app.다른_이름으로_저장.Edit1.SetEditText("c:\python\code\samplecode.py")
 
# "파일이름" 콤보박스에서 파일 종류를 선택 합니다.
app.다른_이름으로_저장.ComboBox2.Select("모든 파일")
 
# "파일형식" 콤보박스에서 인코딩을 선택 합니다.
app.다른_이름으로_저장.ComboBox3.Select("UTF-8")
 
# 바로 저장 버튼을 누르면 미처 콤보 박스가 안 바꿔져 에러가 나서 1초 시간을 주었습니다
import time
time.sleep(1.0)
 
# 저장 버튼을 누릅니다.
app.다른_이름으로_저장.Button1.click()