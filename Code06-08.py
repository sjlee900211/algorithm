## 함수
def isStackFull() : # 스택이 꽉 찼는지 확인
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else :
        return False

def push(data) : # 푸쉬
    global SIZE, stack, top
    if (isStackFull == True) :
        print('Stack is full!')
        return
    top += 1
    stack[top] = data
    

## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


## 메인
push('커피')
push('코코아')
push('홍차')
print('바닥 |', stack)

push('녹차')
print('바닥 |', stack)