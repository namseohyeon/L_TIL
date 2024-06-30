T = int(input())
x = []

for i in range(T):
    a,b = map(int, input().split())
    x.append(a)
    x.append(b)

for j in range(0,len(x), 2):
    print(x[j] + x[j+1]) 
    
