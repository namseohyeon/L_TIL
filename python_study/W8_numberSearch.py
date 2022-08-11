import sys
N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

def search(A,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if A[mid] == target:
            return 1
        elif A[mid] > target:
            end=mid-1
        else:
            start = mid + 1
    return 0
start = 0
end = N - 1
for i in arr:
    print(search(A,i,start,end))
