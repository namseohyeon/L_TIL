#방법 1
x=input()
x=sorted(x)
list = []

sum,count = 0,0
for i in x:
    if(i.isdigit()):
        sum += int(i)
        count += 1
    else:
        list.append(i)
list.append(str(sum))

print(''.join(list))

#방법 2
# x=input()
# x=sorted(x)
# list = []

# sum,count = 0,0
# for i in x:
#     if(i.isdigit()):
#         sum += int(i)
#         count += 1
# for j in range(0,count+1):
#     x.pop(0)

# x.append(sum)
# for k in x:
#     print(k, end="")

#방법 3(해답)
# data = input()
# result = []
# value = 0

# for i in data:
#     if i.isalpha():
#         result.append(i)
#     else:
#         value += int(i)
# result.sort()
# if value != 0:
#     result.append(str(value))

# print(''.join(result)) #리스트를 공백없이 쭉 나열, 리스트의 요소가 문자면 가능




