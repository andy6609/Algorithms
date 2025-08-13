#3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0 :
    print (a)

if b % 2 == 0 : 
    print (b)

if c % 2 == 0 :
    print (c)


""" 
파이썬에서 콜론의 역할 : 여기서부터 새로운 코드 블록이 시작 된다 
if 조건식:
    # 이 안이 코드 블록
 
Indentation (들여쓰기)의 의미 : 파이썬은 { } 중괄호로 블록을 표시하는 대신 들여쓰기로 블록을 구분합니다.

if a%2==0:
    print(a)   # ← 이 줄은 if 안에 속함
print("끝")    # ← 이 줄은 if 밖에 있음   ===>> 보통 space 4 칸 (파이썬 권장 방식 PEP8)

"""