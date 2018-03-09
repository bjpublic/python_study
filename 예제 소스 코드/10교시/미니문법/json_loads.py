import json

# 딕셔너리 형태의 JSON 데이터를 읽어옵니다.
my_json = '{"cat": 3, "dog": 10, "pig": 2}'
to_dictionary = json.loads(my_json)

# 리스트 형태의 JSON 데이터를 읽어옵니다.
my_json2 = '["cat", "dog", "pig"]'
to_list = json.loads(my_json2)

# 변수 타입과 내용 출력합니다.
print(type(to_dictionary))
print(to_dictionary['cat'])

# 변수 타입과 내용 출력합니다.
print(type(to_list))
print(to_list[0])