# 5. 사용자로부터 두 개의 정수를 입력받아 사칙연산 계산 결과를 출력하는 프로그램을 작성하라. 예를 들어 사용자가 입력한 수가 10과 20일 때, 프로그램의 실행 결과는 다음과 같다.

def Cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

a = int(input("첫번째 정수를 입력해 주세요: "))
b = int(input("두번째 정수를 입력해 주세요: "))

Cal(a,b)