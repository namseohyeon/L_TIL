#0,1을 제외하고는 x를 하는 것이 큰 수를 찾는방법
n = input()

result = int(n[0]) #0번째 인덱스를 넣어서 새로운 숫자앞에 부호를 지정할 수 있게 함

for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or result <= 1: #수가 0,1일 때 혹은 결과 값이 현재 2보다 작다면 +
        result += num
    else:
        result *= num

print(result)

