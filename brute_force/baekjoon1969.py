from operator import index
import sys
input = sys.stdin.readline

#N개의 길이M인 DNA가 주어짐, 각 자리가 다른게 가장 적은 DNA 구하기
N, M = map(int, input().split())

DNA = [list(input().strip()) for _ in range(N)]
cnt = 0
answer = ''

for i in range(M):
    count = [0,0,0,0] # A,C,G,T 개수
    for j in range(N):
        if DNA[j][i] == "A" : count[0] += 1
        elif DNA[j][i] == "C" : count[1] += 1
        elif DNA[j][i] == "G" : count[2] += 1
        else : count[3] += 1
    idx = count.index(max(count))
    # 해밍 디스턴스는
    hamming = N - count[idx]
    cnt += hamming
    if idx == 0:
        answer += "A"
    elif idx == 1 :
        answer += "C"
    elif idx == 2:
        answer += "G"
    elif idx == 3:
        answer += "T"
print(answer)
print(cnt)
    

        
