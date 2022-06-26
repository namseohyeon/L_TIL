def Cal(n1,Oper,n2):
    if Oper == "+":
        print("계산기: ",n1,"+",n2,"=",n1+n2)
    elif Oper == "-":
        print("계산기: ",n1,"-",n2,"=",n1-n2)
    elif Oper == "*":
        print("계산기: ",n1,"*",n2,"=",n1*n2)
    elif Oper == "/":
        if(n2 == 0):
            print("0으로 나눌 수 없어요")
        else:
            print("계산기: ",n1,"/",n2,"=",n1/n2)
    elif Oper == "**":
        print("계산기: ",n1,"**",n2,"=",n1**n2)

n1 = int(input("첫번째 수를 입력해주세요: "))
n2 = int(input("두번째 수를 입력해주세요: "))
Oper = input("연산자를 입력해주세요: ")

Cal(n1,Oper,n2)

