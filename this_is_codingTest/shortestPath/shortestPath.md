## 최단 경로 알고리즘
- 가장 짧은 경로를 찾는 알고리즘
- 문제 상황
    - 한 지점에서 다른 한 지점까지의 최단 경로
    - 한 지점에서 다른 모든 지점까지의 최단 경로
    - 모든 지점에서 다른 모든 지점까지의 최단 경로
- 각 지점은 그래프에서 노드로 표현
- 지점간 연결된 도로는 그래프에서 간선으로 표현

### 다익스트라 최단 경로 알고리즘
- 특정한 노드에서 출발하여 다른 모든로 가는 최단 경로를 계산
- 음의 간선이 없을떄 정상적으로 동작
    - 현실세계의 간선은 음의 간선으로 표현되지 않음
- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류
    - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정 반복
- 동작과정
    1. 출발노드 설정
    2. 최단 거리 테이블 초기화
    3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
    5. 위 과정에서 3번 4번을 반복
- 특징:
    - 그리디 알고리즘: 매 상황에서 방문하지 않은 가장 비용이 적은 오드를 선택해 임으의 과정 반복
    - 단계를 거치며 한번 처리된 노드의 최단거리는 고정되어 더 이상 변화x
        - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있음
    - 다익스트라 알고리즘을 수행한 뒹 테이블에 각 노드까지의 최단 거리 정보 저장
        - 완벽한 형태의 최단 경로를 구하여면 소스코드에 추가적인 기능을 넣어야함
- 간단한 구현방법
    - 단계마다 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인
```
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수 입력받기
n, m = map(int,input().split())
#시작 노드 번호를 입력 받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False]*(n+1)
#최단 거리 테이블은 모두 무한으로 초기화
distance =[INF]*(n+1)

#모든 간선 정보 받기
for _ in range(m):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))
#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index
def di(start):
    #시작 노드에 대해서 초기화
    distance[strat] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smaillest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            const = distance[now]+j[i]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance(j[0]):
                distance[j[0]] = cost

#다익스트라 알고리즘을 수행
di(start)

#모든 노드로 가기 위한 최단 고리 출력
for i in range(1,n+1):
    #도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```
- chd o(V)번에 걸쳐서 최단거리가 가장 짧은 노드를 매번 선형 탐색 필요
- 전체 시간 복잡도 o(V^2)
- 노드 개수가 5000이하라면 문제 해결 가능

### 우선순위 큐
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 가치가 높은 물건 데이터부터 꺼내서 확인하는 경우 사용
- 힙
    - 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
    - 최소 힙과 최대 힙이 있음
    - 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용
    - 리스트: 삽입시간O(1), 삭제시간 O(N)
    - 힙: 삽입시간O(logN), 삭제시간 O(logN)
<!-- <table>
    <tr><td>자료구조</td><td>추출되는 데이터</td></tr>
    <tr><td>스택</td><td>자장 나중에 삽입된 데이터</td></tr>
    <tr><td>큐</td><td>가장 먼저 삽입된 데이터</td></tr>
    <tr><td>우선순위 큐</td><td>가장 우선순위가 높은 데이터</td></tr>
</table>
<br> -->
```
#최소 힙
import heapq

def heapsort(iterable):
    h =[]
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in rnage(len(h)):
        result.append(headp.headpop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```
```
#최대 힙
import heapq

def heapsort(iterable):
    h =[]
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in rnage(len(h)):
        result.append(-headp.headpop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```