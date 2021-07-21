## 함수부
def add_data(friend) : # 함수 = FUnction = 기능
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend


## 전역변수
katok = [] # 빈 배열


## 메인코드
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)