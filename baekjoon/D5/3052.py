datas = []
for i in range(10):
    x=int(input())
    y=x%42
    datas.append(y)
print(len(list(set(datas))))
#set은 중복제거