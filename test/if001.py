x = 95
if x >= 90 :
    print("Pass")
    
value = [70, 80, 90, 95]
i = -1
for i in range(len(value)) :
    if (value[i] >= 90) :
        print(value[i], "축하합니다.")
        print("당신은 합격입니다.")
    else :
        print(value[i],"죄송합니다.")
        print("당신은 불합격입니다.")