# 시간 문제
# 가능한 모든 시각의 경우를 하나씩 세서 모두 풀 수 있는문제
# 완점 탐색 문제 유형 -> 가능한 경우의 수를 모두 검사해보는 탐색 방법 
# 시각을 단순히 1씩 증가시키면서 3이 하나라도 포함되어 있는 지 확인

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):

            if '3' in str(i) + str(j) + str(k):
                count +=1
print(count)
