# import sys
# N = int(input())
# arr = [0]*N
# count = [0]*(N+1)
# for i in range(N):
#     arr[i] = int(input())
# for i in sorted(arr):
#     sys.stdout.write(i)

N = int(input())
count = [0]*(N+1)
for i in range(N):
    num = int(input())
    count[num] += 1 

for i in range(num):
    for j in range(count[i]):
        print(i)