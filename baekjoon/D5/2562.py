big =0
count = 0
for i in range(1,10):
    x = int(input())
    if x > big:
        big = x
        count = i
print(big)
print(count)
