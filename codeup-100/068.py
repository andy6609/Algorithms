# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
# 90 ~ 100 : A
# 70 ~   89 : B
# 40 ~   69 : C
#   0 ~   39 : D
# 로 평가되어야 한다.

score = int(input("type your score: "))

if 0 <= score <= 100: 
    if score >= 90:
        print("A")
    elif score >= 70:
        print("B")
    elif score >= 40:
        print("C")
    else:
        print("D")

else: 
    print ("wrong input score.")




"""
input () 함수의 첫번째 인자는 prompt message (안내 문구) 역할을 한다

print("type yout score (0~100): ") 
score = input()

이렇게 해도 되지만 input 에 바로 string 을 넣어도 된다

--- code up simple answer ---
score = int(input())

if score >= 90:
    print ("A")
else: 
    if score >= 70:
        print ("B")
    else:
        if score >= 40:
            print("C")
        else:
            if score >= 0:
                print("D")


"""