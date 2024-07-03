s= input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# 결과를 저장할 리스트
positions = []

# 각 알파벳에 대해 위치 찾기
for letter in alphabet:
    positions.append(str(s.find(letter)))

# 결과 출력
print(' '.join(positions))

#find 함수는 문자열에서 특정 문자열(또는 문자)의 첫 번째 등장 위치를 찾는 함수
