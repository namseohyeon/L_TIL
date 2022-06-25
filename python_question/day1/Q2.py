# 2^1부터 2^5까지 결과를 출력하는 프로그램을 작성하라. 단, 거듭제곱 연산자(*)를 사용하지 않아야 한다. 출력결과는 다음과 같다.

def mul(i,j):
    x = 1
    for z in range (j):
        x *= i
        print(x)
    return x

mul(2,6)



