from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.compat import range
 
# 엑셀을 읽어 옵니다.
wb_read = load_workbook(filename = 'result.xlsx')
 
# 이름이 output 인 sheet 를 가져옵니다.
my_sheet = wb_read['output']
 
# A1, B2 값을 출력합니다.
print ("A1 : " + my_sheet['A1'].value)
print ("B2 : " + my_sheet['B2'].value)
