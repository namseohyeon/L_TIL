# N, K=map(int,input().split())

# arr=list(map(int,input().split()))

# count = int(0)
# for i in range(len(arr)):
#     max = i
#     for j in range(i+1, len(arr)):
#         if arr[max] > arr[j]:
#             arr[max], arr[j] = arr[j] ,arr[max]
#             count += 1
#             print(arr)
#             if(count == K):
#                 print(arr[max],arr[j])
#             max = j
# if count < K:
#     print(-1)
            

# print(arr)

N, K=map(int,input().split())

arr=list(map(int,input().split()))

count = int(0)
for i in range(len(arr)-1,0,-1):
    max = i
    for j in range(i-1,-1,-1):
        if arr[max] < arr[j]:
            arr[max], arr[j] = arr[j] ,arr[max]
            count += 1
            if(count == K):
                print(arr[j],arr[max])
            max = j
if count < K:
    print(-1)
            
print(arr)







