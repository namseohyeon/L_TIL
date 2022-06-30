
def sum(x,y,z):
    sum = 0
    for i in range(x,y+1,z):
        sum += i
    return sum

x=int(input("첫번째 숫자를 입력하시오: "))
y=int(input("두번째 숫자를 입력하시오: "))
z=int(input("더할 숫자를 입력하시오: "))

print("%d+%d+...+%d는 %d입니다." %(x,x+z,y,sum(x,y,z)))