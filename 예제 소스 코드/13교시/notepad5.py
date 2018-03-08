from pywinauto.application import Application
 
# 메모장를 띄웁니다.
app = Application().start("notepad.exe")
 
# 메모장에 code를 적습니다.
app.UntitledNotepad.Edit.type_keys("print {(}'test'{)}", with_spaces = True)
 
# "파일 > 저장" 메뉴를 실행합니다.
app.UntitledNotepad.menu_select("파일(&F)->저장(&S)")
 
# "다른 이름으로 저장" 창의 속성을 리스트업 합니다.
app.다른_이름으로_저장.print_control_identifiers()
