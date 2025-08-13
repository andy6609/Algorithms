#평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

#평가 내용
#평가 : 내용
#A : best!!!
#B : good!!
#C : run!
#D : slowly~
#나머지 문자들 : what?

Eval = input("type your evalutation: ")

if Eval == "A":
    print("best!!!")
elif Eval == "B":
    print("good!!") 
elif Eval == "C":
    print("run!")
elif Eval == "D":
    print("slowly~")
else:
    print("what?")
    
    
# elif 는 앞의 조건이 안맞을떄 다음조건을 확인. else 는 위의 어떤 조건도 맞지 않을떄 확인 
# 이렇게 되면 else 는 if = D 에서만 valid 하다 그래서 A 를 타이핑 해도 what? 이 같이 나온다

""" 
if Eval == "A":
    print("best!!!")
if Eval == "B":
    print("good!!")
if Eval == "C":
    print("run!")
if Eval == "D":
    print("slowly~")
else:
    print("what?")
"""