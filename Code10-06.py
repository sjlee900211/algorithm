## 별모양 출력하기 -> 입력한 숫자만큼 차례대로 별모양을 출력
def printStar(n):
    if n > 0 :
        printStar(n-1)
        print('★ ' * n)

printStar(5)