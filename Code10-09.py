##  랜덤하게 생성한 배열의 합계 구하기
import random

def arySum(arr, n) :
    if n <= 0 :
        return arr[0]
    return arySum(arr, n-1) + arr[n]

ary = [random.randint(0, 255) for _ in range (random.randint(10,20))]
print(ary)
print('배열 합계->', arySum(ary, len(ary)-1) ) 