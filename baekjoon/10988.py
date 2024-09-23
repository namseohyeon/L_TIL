#10988
N=input()
for i in range(len(N) // 2):
    if N[i] != N[-i - 1]:
        print(0)
        break
else:
    print(1)
