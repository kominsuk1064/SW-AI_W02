# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

c = int(input())

for _ in range(c):
    data = list(map(int, input().split()))

    n = data[0]
    scores = data[1:]

    average = sum(scores) / n

    count = 0
    for score in scores:
        if score > average:
            count += 1

    ratio = (count / n) * 100

    print(f"{ratio:.3f}%")