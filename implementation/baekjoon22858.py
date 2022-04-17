import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# K번 카드를 섞은 후 카드의 배치
after_shufle = list(map(int,input().split()))
D = list(map(int, input().split()))

# D규칙에따라 거꾸로 보내면 끝.
# 섞은만큼 거꾸로 
for _ in range(K):
    P = [0]*N
    for i in range(N):
        P[D[i]-1]= after_shufle[i]
    after_shufle = P
print(*after_shufle)
