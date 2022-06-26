#1~3. 다음 표를 참고해 식재료별 칼로리를 식재료별_칼로리라는 이름의 사전으로 정의해 보라. 이 사전은 음식의 이름을 키로, 칼로리를 값으로 저장한다.

ingredient_Calories = { "밀가루":364, "피망":20.1, "올리브": 115,"돼지고기": 242.1}


def Calories(a,b):
    # ingredient_Calories["c"] = 402.5
    if a in ingredient_Calories:
        ingredient_Calories[a] = float(ingredient_Calories.get(a))/100.0 * b
        return(ingredient_Calories[a])
    elif(a == "치즈"):
        ingredient_Calories[a] = 402.5
        ingredient_Calories[a] = float(ingredient_Calories.get(a))/100.0 * b
        return(ingredient_Calories[a])
    else:
        return 0
    


a = input("음식 종류를 입력해주세요: ")
b = float(input("음식의 섭취량을 입력해주세요: "))

cal = Calories(a,b)
print(cal)

