# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

def multiplication(A, B, C):
    if B == 1:
        return A % C
    
    division = multiplication(A, B // 2, C)

    if B % 2 == 0:
        return (division * division) % C
    else:
        return (division * division * A) % C

A, B, C = map(int, input().split())
print(multiplication(A, B, C))