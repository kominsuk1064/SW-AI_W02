# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

word = input().upper()

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = []

for a in alphabets:
    cnt.append(word.count(a))

max_value = max(cnt)

if cnt.count(max_value) > 1:
    print("?")
else:
    i = cnt.index(max_value)
    print(alphabets[i])