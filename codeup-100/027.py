#10진 정수 입력받아 16진수로 출력하기 

a = input()
n = int(a)

print ('%x' %  n)

#n = 255
#print("16진수는 %x" % n)        # 옛날 스타일
#print("16진수는 {}".format(n))  # format() 스타일
#print(f"16진수는 {n:x}")        # f-string 스타일 (추천!)