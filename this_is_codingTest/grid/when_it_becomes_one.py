from re import L
from unittest import result


N,K = input("").split() #입력받은 값을 공백 기준으로 분리

count  = 0
N = int(N)
K = int(K)
while N!=1:
    if(N%K==0): #1. N을 K로 나눈다
        N/=K 
        count +=1
        #print(count)
    else: #2. N에서 1을 뺀다
        N -= 1
        count +=1
        #print(count)

print(count)

# #시간 복잡도를 줄일 수 있는 코드
# n,k = map(int,input().split())  
# result = 0

# while True:
#     #n이 k로 나눠 떨어지는 수가 될 때까지 빼기
#     #n이 k로 나눠떨어지지 않을 때 가장 가까운 수 찾기-> k로 나눠 떨어지는 수가 타켓이됨
#     target=(n//k)*k 
#     result += (n-target) #연산 수행 횟수
#     n = target
#     #n보다 k가 작을 때 반복문 탈출
#     if n<k:
#         break
#     result +=1
#     n//=k

# #마지막 남은 수에 대하여 1씩 빼기
# result += (n-1)
# print(result)


