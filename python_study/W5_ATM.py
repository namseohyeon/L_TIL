# x = int(input())
# time = list(map(int,input().split()))
# time.sort()
# print(time)

# sum,count = 0,len(time)
# def time(count):
#     if count == 0:
#         return 
#     sum +=time[0]
#     count -= 1
#     time(count)
# print(sum)


x = int(input())
time = list(map(int,input().split()))
time.sort()
time = 0
result = 0
for i in range(x):
    sum +=time[i]
    result +=sum
print(result)