N,X = map(int,input().split())
S = []
count = 0
data =list(map(int,input().split()))

for i in data:
    if (X>i):
        S.append(i)
print(*S)