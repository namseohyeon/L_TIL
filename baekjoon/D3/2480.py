A, B, C=map(int,input().split())
count = 0
if(A==B):
    if(B==C):
        count = 3
    else:
        count = 2
elif(B==C):
    if A==C:
        count = 3
    else:
        count = 2
        A = B
elif(A==C):
    if A==B:
        count = 3
    else:
        count =2
else:
    count = 1
    if(A>B):
        if (B>C):
            big = A
        else:
            if(A>C):
                big = A
            else:
                big = C
    else:
        if (B>C):
            big = B
        else:
            if(A>C):
                big = B
            else:
                big = C


if count == 3:
    print(10000+(A)*1000)
elif count == 2:
    print(1000+(A)*100)
else:
    print(big*100)


#개 똑똑한 chatGpt코드
# a, b, c = map(int, input().split())

# # 같은 눈이 3개 나오는 경우
# if a == b == c:
#     prize = 10000 + a * 1000
# # 같은 눈이 2개 나오는 경우
# elif a == b or a == c:
#     prize = 1000 + a * 100
# elif b == c:
#     prize = 1000 + b * 100
# # 모두 다른 눈이 나오는 경우
# else:
#     prize = max(a, b, c) * 100

# print(prize)