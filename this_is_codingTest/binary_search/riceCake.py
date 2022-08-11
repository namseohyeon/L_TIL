#N은 떡 개수, M은 떡 길이
N,M=map(int,input().split())

#떡의 개별 높이
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0
# arr.sort()

while start<=end:
    total = 0
    mid = (start+end)//2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < M:
        end=mid-1
    else:
        result = mid
        start=mid+1
print(result)

# result = search(arr,target,0,N-1)

if result == None:
    print("원소 존재 x")
else:
    print(result + 1)

