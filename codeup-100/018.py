# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

# split() 괄호안에 아무것도 안넣으면 공백 기준으로 문자열로 나눔 
# print("A", "B", "C", sep='-')
# 출력: A-B-C
# print("2025", "08", "07", sep='/')
# 출력: 2025/08/07

a, b = input().split(':')
print (a,b, sep=':') 
# split 기준은 : 이니까 입력시에 반드시 : 넣어 줘야 함 

# time_str = input()
#if ':' in time_str:
#    a, b = time_str.split(':')
#    print(a, b, sep=':')
#else:
#    print("입력 형식이 올바르지 않습니다. 예: 13:23")