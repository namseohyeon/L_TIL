#1316
N = int(input())
word = []
group_word_count = 0
for i in range(N):
  word = input()
  seen = []
  is_group_word = True

  for i in range(len(word)):
    if word[i] not in seen:
      seen.append(word[i])
    elif word[i] != word[i-1]:
      is_group_word = False
      break

  if is_group_word:
    group_word_count += 1
print(group_word_count)
