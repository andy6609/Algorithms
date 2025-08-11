#정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.

a,b = map(int, input().split())
print(a<<b)

# 2 3 을 넣으면 2에다가 2의3승 배가 곱해짐. 3만큼 시프트 됐기 떄문에 2의 b승. 한번 shift - 2배, 두번 shift - 2의 2승배, 3번 shift - 2의 3승배. 