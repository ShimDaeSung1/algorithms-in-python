import re

# ^ 해당 패턴으로 시작
# ? 해당 패턴을 0번 또는 1번
# $ 해당 패턴으로 끝
# + 해당 패턴이 하나 이상

p = re.compile('^[A-F]?A+F+C+[A-F]?$')

t = int(input())

for _ in range(t):
    str = input().strip()
    if p.match(str):
        print("Infected!")
    else:
        print("Good")