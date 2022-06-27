
def para_func(n1,n2,n3=0,n4=0,n5=0,n6=0,n7=0,n8=0,n9=0,n10=0):
    sum = n1+n2+n3+n4+n4+n5+n6+n7+n8+n9+n10
    return sum

sum1 = para_func(10,20)

sum2 = para_func(10,20,30,40,50,60,70,80,90,100)

print("매개변수가 2개인 함수를 호출한 결과 =>", sum1)

print("매개변수가 10개인 함수를 호출한 결과 =>", sum2)

