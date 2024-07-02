datas = [ i for i in range(1,31)]
for i in range(28):
    x = int(input())
    datas.remove(x)
#for i in range(len(datas)):
print(*datas, sep="\n")
