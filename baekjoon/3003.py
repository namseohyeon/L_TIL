#3003
chess = [1,1,2,2,2,8]
need = []
piece=list(map(int,input().split()))
for i in range(len(chess)):
    x=chess[i] - piece[i]
    need.append(int(x))
print(*need)
