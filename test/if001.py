x = 95
if x >= 90 :
    print("Pass")
    
value = [70, 80, 90, 95]

for value in range(len(value)) :
    if (value >= 90) :
        print(value, "축하합니다.")
        print("당신은 합격입니다.")
    else :
        print(value,"죄송합니다.")
        print("당신은 불합격입니다.")