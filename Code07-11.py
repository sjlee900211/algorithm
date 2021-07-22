## 함수
def isQueueFull() : 
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front :
        return True
    else : 
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False
    
def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None    
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front]
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None
    return queue[(front+1) % SIZE]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = 0, 0

## 메인
## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<---', queue, '<--입구')
retData = deQueue()
print('입장 손님-->', retData)
retData = deQueue()
print('입장 손님-->', retData)
retData = deQueue()
print('입장 손님-->', retData)
retData = deQueue()
print('입장 손님-->', retData)
print('출구<---', queue, '<--입구')
enQueue('수진')
print('출구<---', queue, '<--입구')
enQueue('혜리')
print('출구<---', queue, '<--입구')
enQueue('미나')
print('출구<---', queue, '<--입구')

# queue = ['화사', '솔라', '문별', '휘인', '선미', None]
# front = -1
# rear = 3
# print(isQueueFull())