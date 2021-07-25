## 함수
def binSearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary) - 1
    
    while (start <= end) :
        mid = (start+end) // 2
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid -1     
    
    return pos

## 전역
dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162 # 할머니 키

## 메인
print('배열->', dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
    print(' 없다...')
else :
    print(findData, '는', position, '위치에 있음')
    
    이거를 형상관리를 넣어서 올려야하는데이것도 배워야함