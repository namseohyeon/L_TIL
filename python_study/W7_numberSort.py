N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())

# arr.sort()
for i in sorted(arr):
    print(i)