# regular expression 모듈을 불러 옵니다.
import re
 
# 정규표현식 패턴을  등록합니다(처음 시작이 < 이고 > 로 닫히는 단어).
# 패턴을 괄호로 감쌉니다.
pattern = re.compile("(^<.*>)")  
 
# reg.txt 파일을 한줄 한줄 가져와서(enumerate) 루프를 돌리면서,
for i, line in enumerate(open('reg.txt')):
# 해당 줄에서 원하는 패턴을 모두 찾아 한건 한 건 꺼내어서,
    for match in re.finditer(pattern, line):
# 찾은 값을 출력합니다.
        print (match.groups())
