N, M = map(int,input().split())
baskets = list(range(1, N+1)) 

for j in range(M):
    x, y = map(int,input().split())
    baskets[x-1], baskets[y-1] = baskets[y-1], baskets[x-1]

print(*baskets)

