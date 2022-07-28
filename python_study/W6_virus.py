N=int(input())
M=int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph[1][1])
visited=[False]*9
count = int(0)

def dfs(graph, v, visited):
    global count
    visited[v] = True
    # print(v, end="")
    for i in graph[v]:
        print(graph[i]) #[2,3]중 2와 연결되어있는 노드들이 출력됨
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(count)
print(graph)