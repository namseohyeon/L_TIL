N,K = input("").split() #입력받은 값을 공백 기준으로 분리
#1. N에서 1을 뺀다
#2. N을 K로 나눈다
count  = 0
N = int(N)
K = int(K)
while N!=1:
    if(N%K==0):
        N/=K
        count +=1
        #print(count)
    else:
        N -= 1
        count +=1
        #print(count)

print(count)
