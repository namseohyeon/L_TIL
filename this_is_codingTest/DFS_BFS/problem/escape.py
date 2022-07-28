from collections import deque
N,M=map(int,input().split())

#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(0,N):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


#DFS로 특정 노드를 방문하고, 연결된 모든 노드들도 방문
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복하기
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x+ dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx <= -1 or nx >=N or ny <= -1 or ny >=M:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드가 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[N-1][M-1]

print(bfs(0,0))
