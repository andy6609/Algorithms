# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
# break ??

n = input() # 인풋을 while 전에서 한번만 받으면 당연히 while 안에서 입력이 바뀌지 않는다. 

while n== True: # n = True 이렇게 표현 하면 비교가 아니라 대입이다. 

    if n == 'q':
        break
