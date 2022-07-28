count=0
def dfs(graph, v, virused):
    global count
    virused[v]=True
    count+=1
    for i in graph[v]:
        print(graph[i])
        if not virused[i]:
            dfs(graph, i, virused)

#컴퓨터 수
n=int(input())
#연결된 컴퓨터 쌍 수
m=int(input())
#루트 비우고 index=1~7
graph=[[]*n for i in range(n+1)]
#[[], [], [], [], [], [], [], []]
for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
#graph[1]=2
#graph[2]=1
#[[], [2], [1], [], [], [], [], []]
print(graph)
virused=[False]*(n+1)
dfs(graph,1,virused)
print(count-1)

#grp[1]=2,5
#grp[2]=1,3
#grp[3]=2
#grp[5]=1
