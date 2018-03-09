from datetime import datetime

# 오늘의 날짜 및 시간을 얻어옵니다.
today = datetime.today()
# 오늘이 몇 번째 요일인지 알아옵니다(0~6:월~일)
weekday = today.weekday()

# 오늘의 날짜를 출력 합니다.
print("today: " + str(today))

# 오늘이 월요일인지 체크해 출력합니다.
if weekday == 0:
    print("today is monday")
else:
    print("today is not monday")