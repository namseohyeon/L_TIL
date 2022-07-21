from collections import deque
 
n=int(input())
list = []

for i in range(1,n+1):
    list.append(i)

dequedate = deque(list)

dequedate.pop()
new = dequedate.append(dequedate.popleft())

# print(deque)


# from collections import deque
# T=int(input());
# dq=deque([*range(1,T+1)]);

# for i in range(T-1):
#     dq.popleft();
#     dq.append(dq.popleft());
#     print(dq);
    
# print(dq[0]);

#123456
#i=0 23456->34562
#i=1 4562->5624
#i=2 624->246
#i=3 46->64
#i=4 4