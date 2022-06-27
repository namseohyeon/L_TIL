# 문제3

# 사용자로부터 정수를 입력받아 그 수의 절댓값을 화면에 출력 하는 함수 print_absolute()를 정의하고 호출해 보라. 실행 결과는 다음과 같다.

def print_absolute(num):
    if num >= 0:
        print(num)
    else:
        print(-num)


num = int(input("정수를 입력해주세요: "))

print_absolute(num)