
n=int(input())
c=1
for i in n:
    stack = []
    if i=="(":
        stack.append(i)
        c+=1
    elif(c==1):
        print("NO")

        
# k=int(input())
# result=[]
# for i in range(k):
#     stk=[]
#     isVPS=True
#     for char in input():
#         if char == '(':
#             stk.append(char);
#         elif char ==')':
#             if stk:
#                 stk.pop();
#             else: #여는 괄호가 없는 경우
#                 isVPS=False;
#                 break;
#     if stk: #여는 괄호가 남는경우
#         isVPS=False;
#     result.append('YES' if isVPS else 'No')

#     # print('YES' if isVPS else 'No')                
# print(result);


# count = int(input())

# for i in range(count):
#     stack = []
#     string = input()
#     for i in string:
#        if i=="(":
#            stack.append(i)
#        elif i==")" and "(" not in stack:
#            stack.append(i)
#        elif i==")":
#            stack.pop()
#     if len(stack) > 0:
#         print(len(stack))
#         print("NO")
#     else:
#         print("YES")