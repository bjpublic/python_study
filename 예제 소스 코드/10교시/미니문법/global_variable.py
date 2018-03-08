# 정의 없이 사용합니다.
def print_global():
    print(a)

# global 로 정의해 사용합니다.
def print_global2():
    global a
    print(a)

# 함수안에 같은 이름의 변수를 만듭니다.
def print_local():
    a = "local a"    
    print(a)

# 글로벌 변수로 간주 될 변수 입니다.
a = "global a"

print_global()
print_global2()
print_local()
