import sys
input = sys.stdin.readline

# n은 당근종류, t는 재배일수
n, t = map(int, input().split())
# carrot = [[w, p]](w:당근 기본 맛, p: 영양제)
carrot = [list(map(int, input().split()))for _ in range(n)]
carrot.sort(key=lambda x : (-x[1], -x[0]))

taste = 0
days = t-1

for w, p in carrot:
    taste += w+(p*days)
    days -= 1

print(taste) 
