## 탐색
+ 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
+ 대표적인 그래프 탐색 알고리즘 DFS,BFS가 있음
+ DFS/BFS은 코테에 매우 자주 등장 유형

#### 스택
+ 먼저 들어온 데이터가 나중에 나가는 선입후출 자료구조
+ 입구와 출구가 동일함
+ 삽입, 삭제 가능 (append와 pop사용)
```
stack = []

stack.append(5)
stack.append(2)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력 인덱스 끝부터
print(stack) #최하단 원소부터 출력 인덱스 0부터
```

#### 큐
- 먼저 들어온 데이터가 먼저 나가는 선입선출 형식의 자료구조
- 입구와 출구가 모두 뚫려 있는 터널 같은 형태
```
from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.popleft()

queue.reverse()
print(queue)
```

#### 재귀함수
+ 자기자신을 다시 호출하는 의미
+ 재귀 깊이 제한 정하지 않으면 -> 오류 메세지와 함께 종류
+ 재귀함수를 문제풀이에서 사용할때는 재귀 함수의 종료조건을 반드시 명시
+ 종료조건을 명시하지 않으면 함수 무한히 호출
+ 유의사항:
    + 이해하기 어려운 코드가 될 수 있음
    + 모든 재귀함수는 반복문을 이용하여 동일한 기능 구현가능
    + 재귀함수가 반복문보다 유리할 수도 분리할 수도 
    + 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부 스택 프레임이 쌓임
         + 스택을 사용할때 구혁상 스택 라이브러리 대신 재귀함수 이용하는 경우가 많음
```
def recursive(i):
    if i == 100:
        return 
    print("재귀함수")
    recursive(i+1)

recursive(1)
```
+ 팩토리얼 구현 예제 (n! = 1x2x3x...x(n-1)xn)
```
#반복적으로 구현
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

#재귀적으로 구현
def factorial_recursive(n):
    if n<= 1:
        return
    return n * factorial(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))
```
+ 최대공약수 계산(유클리드 호제법) 예제
    + 두 자연수 A,B에 대하여(A>B) A를 B로 나눈 나머지를 R
    + 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다
```
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)
gcd(192,162)
```

### DFS
+ DFS는 깊이 우선 탐색 -> 깊은 부분을 우선적으로 탐색하는 알고리즘
+ 스택 자료구조(재귀함수)를 이용
    1. 탐색노트를 스택에 삽입하고, 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있다면 그 노드를 스택에 넣고 방문 처리, 없다면 스택에서 최상단 노드 꺼내기
    3. 더 이상의 2번의 과정을 수행할 수 없을 때까지 반복

```
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end="")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visted=[False]*9 #인덱스0은 안쓰므로 크기 하나크게

dfs(graph, 1, visited)
```

### BFS
+ 너비 우선 탐색 -> 가까운 노드부터 우선적으로 탐색하는 알고리즘
+ 큐 자료구조 이용
    1. 탐색 시작 노드를 큐에 삽입하고, 방문처리
    2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고, 방문 처리
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

```
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end="")
        for i in graph[v]:
            if not visited[i]:
            visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visted=[False]*9 #인덱스0은 안쓰므로 크기 하나크게

bfs(graph, 1, visited)
```