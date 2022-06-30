option=int(input("1.입력한 수식 계산 2. 두 수 사이의 합계: "))

def sum(x,y):
    sum = 0
    for i in range(x,y+1):
        sum += i
    return sum

if(option==1):
    word=input("***수식을 입력하세요***")
    print(eval(word))
elif(option==2):
    x=int(input("***첫번째 수를 입력하세요: "))
    y=int(input("***두번째 수를 입력하세요: "))
    # sum = sum(x,y)
    print("%d+...+%d는 %d입니다." %(x,y,sum(x,y)))
