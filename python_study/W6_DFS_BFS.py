

# N,M,V = map(int,input().split())

# graph = []
# for i in range(0,M):
#     graph.append(list(map(int,input().split())))

# print(graph)
# def dfs(x,y):
#     if x <= -1 or x >=N or y <= -1 or y >=M:
#         return False
#     if graph[v] == 0:
#         return True
#     return False 

# result = 0
# for i in range(M):
#     for j in range(M):
#         #현재 위치에서 DFS 수행
#         if dfs(i,j) == True:
#             result += 1
# print(result)

from collections import deque
import copy

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i]==False:
            dfs(graph,i,visited)
            
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True

