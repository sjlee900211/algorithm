#리스트로 출력하지 않아 원하는 range 값 안나옴
print(range(0,10,1))

#리스트로 출력해서 0부터 9까지의 리스트 값 나옴
print(list(range(0,10,1)))

#0부터 6까지 반복
for a in range(0,6,1) :
    print(a)

#0부터 6까지 2step으로 반복    
for a in range(0,6,2) :
    print(a)

#0부터 9까지 list에 출력하는 다양한 방법
#시작점이 0인 경우 생략가능, step이 1인 경우 생략가능    
print(list(range(0,10,1)))
print(list(range(0,10)))
print(list(range(10)))

#응용
print(list(range(0,20,5)))
print(list(range(-10,0,2)))
print(list(range(3,-10,-3)))
print(list(range(0,-5,1)))