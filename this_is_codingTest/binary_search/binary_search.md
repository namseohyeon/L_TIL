## 이진 탐색 알고리즘
- 순차 탐색: 리스트 안에 있는 특정한 <b>데이터를 찾기 위해 앞에서 부터 데이터를 탐색</b>
- 이진 탐색: <b>정렬되어 있는 리스트</b>에서 <b>탐색범위를 절반씩 좁혀가며 데이터를 탐색하는 방법</b>
    - 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
    - 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 탐색 범위를 절반씩 줄이며, 시간복잡도는 O(logN)을 보장

```
#이진 탐색 소스코드 구현(반복문)
def binary_search(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end=mid-1
        else:
            start = mid + 1
    return None

n, target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소 존재 x")
else:
    print(result + 1)
```
```
#이진 탐색 소스코드 구현(재귀함수)
def binary_search(array,target,start,end):
    while start>end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

n, target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소 존재 x")
else:
    print(result + 1)
```

### 파이썬 이진 탐색 라이브러리
- bisect_left(a,x): 정렬된 순설르 유지하면서 배열a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a,x): 정렬된 순서를 유지하면서 배열a에 x를 삽입할 가장 오른쪽 인덱스 반환
```
from bisect import bisect_left, bisect_right

def count_by_range(a, right_value, left_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index
a=[1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

#값이 [-1,3]범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))
```

### 파라메트릭 서치
- 최적화 문제를 결정문제('예','아니요')로 바꾸어 해결하는 기법
    - 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적인 코테에서 파라메트릭 서치 문제는 이진탐색을 이용하여 해결 가능