N, K = map(int, input().split())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

array1.sort()
array2.sort(reverse=True)

for i in range(0, K):
    if (array1[i] < array2[i]):
        array1[i] = array2[i]

# sum = 0
# for i in range(0, N):
#     sum += array1[i]
# print(sum)
# print(array1)

print(sum(array1))
