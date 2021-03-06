## 함수
class TreeNode() : # 트리노드의 틀(붕어빵 기계)
    def __init__(self) :
        self.left = None
        self.data = None
        self.right = None

## 전역
memory = []
root = None
## 실제 데이터
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']


## 메인
# 첫 노드 생성(약간 다름)
node = TreeNode()
node.data = nameAry[0]
root = node # 핵심
memory.append(root)

for name in nameAry[1:] : # ['레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스', ...]
    node = TreeNode()
    node.data = name

    current = root
    while True : # 몇번 비교해야 자리잡을지 모름.
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진 탐색 트리! 구성 완료')

## 데이터를 검색(=탐색)할 때 완전 효율적
# findName = '마마무'
findName = '핑클'

current = root
count = 0
while True :
    count += 1
    if current.data == findName :
        print(findName, '오예 찾았다!!', count, "번")
        break
    elif findName < current.data :
        if current.left == None :
            print(findName, '아쉽다... 못 찾음')
            break
        current = current.left
    else :
        if current.right == None :
            print(findName, '아쉽다... 못 찾음')
            break
        current = current.right