# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

expression = input()

minus = expression.split('-')

result = sum(map(int, minus[0].split('+')))

for i in minus[1:]:
    result -= sum(map(int, i.split("+")))

print(result)