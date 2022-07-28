N=int(input())
count = 0
def dfs(x,y):
    global count
    #주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >=N or y <= -1 or y >=N:
        return False
    #현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 1:
        #해당노드 방문처리
        graph[x][y] = 0
        count += 1
        #상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        
        return True
    return False 
num = []
graph = []
for i in range(0,N):
    graph.append(list(map(int,input())))

result = 0
for i in range(N):
    for j in range(N):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            # print(graph)
            result += 1
            num.append(count)
            count = 0

print(result)
num.sort()
for i in num:
    print(i)
  