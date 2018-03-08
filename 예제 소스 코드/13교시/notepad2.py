from pywinauto.application import Application

# 메모장를 띄웁니다.
app = Application().start("notepad.exe")

# "도움말 > 메모장 정보" 메뉴를 선택합니다.
app.UntitledNotepad.menu_select("도움말(&H)->About Notepad")
 
# "확인" 버튼을 눌러서 다이얼로그를 닫습니다.
app.AboutNotepad.OK.click()

# 메모장에 내용을 적습니다.
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
