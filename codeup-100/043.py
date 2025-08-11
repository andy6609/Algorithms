#실수 2개(f1, f2)를 입력받아
#f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

# f1,f2 = float(input().split())  => 이렇게 안된다니까 split 으로 마무리 돼서 리스트가 나오는데 float 으로 어떻게 list 반환 할거임? 한꺼번에 하고 싶으면 map 

f1, f2 = map(float, input().split())
print(format (f1//f2, ".3f"))