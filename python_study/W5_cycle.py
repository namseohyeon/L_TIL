# x=list(map(int,input()))

# sum=x[0]+x[1]
x=input()
List = [x[0],x[1]]

while True:
    # sum = int(x[0])+int(x[1])
    # print(sum)
    # sum =sum + int(x[1])
    # print(sum)
    List.append(int(List[0])+int(List[1]))
    print(List)
    if x == List[2]:
        break
    List.pop(0)
print(List)
