from posixpath import split


N, K = map(int, input().split())

arr = list(map(int, input().split))

for i in range(len(arr)-1, 0, -1):
    max = i
    for j in range(i-1, -1, -1):
        if(arr[max] > arr[j]):
            arr[max], arr[j] = arr[j], arr[max]
            max = j

