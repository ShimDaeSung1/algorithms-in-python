import itertools
import sys
input = sys.stdin.readline

# permutations(객체, r) : 순열 ([사과,배]와 [배,사과]를 다르게)
# combinations(객체, r) : 조합 ([사과,배]와 [배,사과]를 같게)
# product(반복 가능한 객체, repeat = 2) : 중복 순열 ([배,배], [사과, 사과]허용, [사과,배], [배,사과]를 다르게)
# combinations_with_replacement(반복 가능한 객체, repeat = 2) : 중복 + 조합

# N은 아이스크림 종류, M은 섞어 먹으면 안 되는 조합의 개수
N, M = map(int, input().split())

no_mix = [list(map(int, input().split())) for _ in range(M)]
ice = [[False]*(N+1) for _ in range(N+1)]
ls = []
for i in range(1,N+1):
    ls.append(i)

rst = list(itertools.combinations(ls, 3))

for i in no_mix:
    a, b = i
    ice[a][b] = True
    ice[b][a] = True
rest = 0
for i in rst:
    a,b,c = i
    if ice[a][b] or ice[a][c] or ice[b][c] :
        continue
    rest += 1
print(rest)


