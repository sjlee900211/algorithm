## 구구단 출력하기->2단부터 9단까지
def gugudan(dan, num) :
    print("%d x %d = %d" % (dan, num, dan*num))
    if num < 9 :
        gugudan(dan, num + 1)

for dan in range(2, 10) :
    print("## %d단 ##" % dan)
    gugudan(dan, 1)