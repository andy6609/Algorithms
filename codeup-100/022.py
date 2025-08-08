# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자
# 슬라이스 사용. print (s[0:2]), 0 부터 1까지만 프린트 한다는 뜻.

s = input ()

print (s[0:2])
print (s[2:4])
print (s[4:6])

# -- way 2 -- 
#YY = s[0:2]
#MM = s[2:4]
#DD = s[4:6]

#print (YY, MM, DD)




#YY, MM, DD = input()     => 이코드는 오류가 난다. WHY? input() 이렇게만 사용하면 하나의 문자열만 반환 하기 때문 
#print(YY+MM+DD)