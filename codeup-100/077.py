# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

n = int(input())

# 여기서 while 을 써도 되고 for 를 써도 된다
s = 0

for i in range (1, n+1):
    if i % 2 == 0:
        s = s + i # i 를 2 로 나눴을때 나머지가 0 이면 s 값에 i 를 더한다. 즉 i 가 짝수이면 더하기 

print (s)