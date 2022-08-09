from bisect import bisect_left, bisect_right
N,x=map(int,input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)

arr.sort()

def count_by_range(a, right_value, left_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index

# 값이 4인 데이터 개수 출력
count=count_by_range(arr,x,x)

if count == 0:
    print(-1)
else:
    print(count)


