## 이진 탐색 알고리즘
- 순차 탐색: 리스트 안에 있는 특정한 <b>데이터를 찾기 위해 앞에서 부터 데이터를 탐색</b>
- 이진 탐색: <b>정렬되어 있는 리스트</b>에서 <b>탐색범위를 절반씩 좁혀가며 데이터를 탐색하는 방법</b>
    - 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
    - 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 탐색 범위를 절반씩 줄이며, 시간복잡도는 O(logN)을 보장

'''
def binary_search(array,target,start,end):
    while start>end:
        mid = (staet+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end=mid-1
        elseL
        start = mid + 1
    return None

n, target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result = None:
    print("원소 존재 x")
else:
    print(result + 1)
```