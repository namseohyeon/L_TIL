from bisect import bisect_left, bisect_right
N = int(input())

A = sorted(map(int,input().split()))

M = int(input())

arr = list(map(int,input().split()))


def count_by_range(a, right_value, left_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index

for i in arr:
    print(count_by_range(A,i,i), end=" ")
