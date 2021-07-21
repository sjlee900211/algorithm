## 함수
class Node() : # 붕어빵 기계
    def __init__(self) :
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    print(current.data, end='  ')
    while current.link != None:
        current = current.link
        print(current.data, end='  ')
    print()


## 전역
memory = []
head, current, pre = None, None, None
# 데이터 집합 (실무 DB, 웹크롤링, 센서신호...)
dataArray = ['다현', '정연', '쯔위', '사나', '지효']


## 메인
# 첫 노드
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)
# 그 외 노드
for data in dataArray[1:] :
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
    
printNodes(head)