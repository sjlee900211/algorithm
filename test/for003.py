names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]

for k in range(len(names)) :
    print(names[k], scores[k])
    
#zip 함수 이용해 반복변수 넣어보기
for name, score in zip(names, scores) :
    print(name, score)