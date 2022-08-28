# N=int(input())
# graph = []

# for _ in range(N):
#     graph.append(list(map(int, input().split())))

# for k in range(N): 
N=int(input())
M=int(input())
INF= 100000000
s = [[INF] * N for i in range(N)]

for i in range (M):
    a, b, c = map(int, input().split()) 
    if s[a-1][b-1] > c:
        s[a-1][b-1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]
for i in s:
    for j in i:
        if j==INF:
            print(0,end="")
        else:
            print(j, end='')
    print()