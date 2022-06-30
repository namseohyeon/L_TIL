# 문제 4

# 약수가 1과 자기 자신뿐인 자연수를 소수(prime number)라 한 다. 어떤 수를 입력받아 그 수가 소수인지를 True 또는 False로 반환하는 함 수 is_prime()을 정의하라. 그 후, 정의한 함수를 이용해 1 이상 100 미만의 모든 소수의 합을 계산하라. 

from tkinter.tix import Tree


s = 0
def is_prime(x):
    count = 0
    for i in range(1,x+1):
        if(x % i == 0):
            count +=1
    if(count == 2):
        return True
    else:
        False

# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return  True

    
def sum(x):
    global s
    if(is_prime(x)):
        s += x
    return s
        

for i in range (1,101):
    s1 = sum(i)
print("합계:",s1)


# x = int(input("값을 입력하시오: "))
# print(sum(x))
