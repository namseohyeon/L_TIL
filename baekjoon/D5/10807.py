N = int(input())
count = 0
data =list(map(int,input().split()))
v = int(input())

for i in data:
    if (v==i):
        count += 1
print(count)