#문제4 다음 세 집합을 각각 파이썬 코드로 정의하라.

# - 한 주의 모든 요일
# - 여러분이 학교나 직장에 가는 요일
# - 여러분이 휴식을 취하는 요일

day = {'월', '화', '수', '목', "금",'토','일'}
working_day = {'월', '화', '수', '목', "금"}
holiday = {'토','일'}

# 문제5

# is_holiday() 함수를 정의하라. 이 함수는 요일을 입력받아 그 요일이 여러분이 쉬는 날이면 True, 아니면 False를 반환한다.

def is_holiday(day):
    if day in holiday:
        return True
    else:
        return False

day = input("무슨 요일?")
happy = is_holiday(day)
print(happy)