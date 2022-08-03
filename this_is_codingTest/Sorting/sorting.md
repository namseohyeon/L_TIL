## 정렬
+ 데이터를 특정한 기준에 따라 순서대로 나열하는 것
+ 일반적인 문제상황에 따라 적절한 알고리즘이 공식처럼 사용

### 선택정렬
+ 처리되지 않은 데이터 중 <b>가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복</b> 
```
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
        min_index=j
    array[i], array[min_index] = array[min_index], array[i]
print(array)
```
+ 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야함
+ 전체 연산 횟수 N + (N-1) + (N-2) + .. + 2
+ 이는 (N^2 + N - 2)/2로 표현할 수 있는데, 빅오 표기법에 따라 O(N^2)이라고 작성

### 삽입정렬
+ 처리되지 않은 데이터를 하나씩 골라 <b>적절한 위치에 삽입</b>
+ 선택정렬보다 어려움 but 더 효율적으로 동작
```
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):
    for j in range(i,0,-1):
    if array[j] < array[j-1]:
        array[j],array[j-1] = array[j-1],array[j]
    else:
        break
print(array) 
```
+ 시간복잡도 O(N^2)
+ 삽입 정렬은 연재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
+ 최선의 경우 O(N)

### 퀵정렬
+ 기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
+ 일반적인 상황에서 가장 많이 사용
+ 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
+ 가장 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(pivot)로 설정
+ 피벗을 기준으로 데이터 묶음을 나누는 작업을 분할이라고 함
+ 빠른이유: 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)
    + 넓이 x 높이 = N x logN
+ 평균 시간 복잡도 O(NlogN)
+ 최악의 경우 O(N^2)의 시간 복잡도를 가짐
```
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left<=right):
    #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left<=end and array[left]<=array[pivot]):
            left += 1
    #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right> start and array[right]>=array[pivot])
            right -=1
        if(left>right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array,0,len(array)-1)
print(array)
```
+ 파이썬의 장점을 살린 방법
```
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0] #피벗의 첫번째 원소
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x <=pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] +  quick_sort(right_side)
print(quick_sort(array))
```

### 계수 정렬
+ 특정한 조건이 부합할 때만 사용할 수 있지만 <b>매우 빠르게 동작하는</b> 정렬 알고리즘
    + 계수정렬은 데이터의 크기 범위가 제한되어 정수형태로 표현할 수 있을 때 사용 가을
+ 데이터의 개수가 N,데이터(양수) 중 최댓값이 K일때 최악의 경우에도 수행시간 O(N+K)보장
```
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1 

for i in range(len(array)):
    for j in range(count[i]):
        print(i, end=" ")
```
+ 시간 복잡도와 공간복잡도는 모두 O(N+K)
+ 계수 정렬은 때에 따라 비효율적임
+ 동일한 값을 가지는 데이터가 여러 개 등장할때 효과적으로 사용 가능

#### 정렬알고림즘 비교
+ 지원하는 표준 정렬 라이브러리는 최악의 경우에도O(NlogN)을 보장하도록 설계
<table>
    <tr><td>정렬 알고리즘</td>><td>평균시간 복잡도</td><td>공간 복잡도</td><td>특징</td><tr>
    <tr><td>선택정렬</td><td>O(N^2)</td><td>O(N)</td><td>아이디어 간단</td><tr>
    <tr><td>삽입정렬</td>><td>O(N^2)</td><td>O(N)</td><td>데이터 거의 정렬되어 있을때 가장 빠름 </td><tr>
    <tr><td>퀵 정렬</td><td>O(NlogN)</td><td>O(N)</td><td>대부분 적합, 충분히 빠름</td><tr>
    <tr><td>계수 정렬</td><td>O(N+K)</td><td>>O(N+K)</td><td>데이터의 크기가 한정되어 있는 경우에만 사용 가능, 매우 빠르게 동작</td><tr>
</table>