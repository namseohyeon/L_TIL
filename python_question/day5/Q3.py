# 문제 3

# 연도와 월을 매개변수로 입력받아, 그 달이 며칠까지 있는지 반환하는 함수 days_in_month()를 작성하라. 이때, 2월의 길이는 윤년인지 아닌지에 따라 다르다. 윤년 계산을 위해 문제 2에서 만든 함수를 활용하라.

def is_leap_year(y):
    if(y % 4 == 0 and y % 100 != 0):
        return True
    elif(y % 400 == 0):
        return True
    else:
       return False

def days_in_month(y,m):
    if(m==1 or 5 or 7 or 8 or 10 or 12):
        print("%s년 %d일은 31일 까지 입니다." %(y,m))
    elif (m==2) :
        if is_leap_year(y):
            print("%s년 %d일은 29일 까지 입니다." %(y,m))
        else:
            print("%s년 %d일은 28일 까지 입니다." %(y,m))
    else:
        print("%s년 %d일은 30일 까지 입니다." %(y,m))

y = int(input("확인해보고 싶은 년도를입력해주세요: "))
m = int(input("확인해보고 싶은 월을 입력해주세요: "))
days_in_month(y,m)