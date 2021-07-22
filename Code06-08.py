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

def isStackEmpty() : 
    global SIZE, stack, top
    if (top == -1) :
        return True
    else:
        return False

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        print ('Stack is empty!')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() : # 다음 확인만!
    global SIZE, stack, top
    if(isStackEmpty()) :
        print('Stack is empty!')
        return None
    return stack[top]

## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


## 메인
push('커피')
push('홍차')
print('바닥 |', stack)
retData = peek()
print('다음에 나올 것-->', retData)

retData = pop()
print('빼낸 것-->', retData)
retData = pop()
print('빼낸 것-->', retData)
retData = pop()
print('빼낸 것-->', retData)