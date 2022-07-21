#체스 나이트 이동 문제
# 내 풀이
# x=input()
# row = int(x[1])
# column = x[0]

# steps = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(-1,-2),(-1,2),(1,-2)]


# dic = {'a':1, 'b':2, 'c':3, 'd':5, 'e':6, 'f':7, 'g':9, 'h':10}

# count = 0
# for k in dic.keys():
#     if(k==column):
#         column = dic.get(k)
#         for step in steps:
#             next_row = row + step[0]
#             next_column = column + step[1]
#             if next_row >= 1 and next_column >= 1 and next_row <=8 and next_column <= 8:
#                 count += 1
# print(count)



from unittest import result


input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a')) + 1
# print(column)

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(-1,-2),(-1,2),(1,-2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_column >= 1 and next_row <=8 and next_column <= 8:
        result +=1

print(result)

