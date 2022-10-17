import sys
input = sys.stdin.readline

#카드의 개수N, M을 넘지 않으면서 M에 최대한 가깝게
N, M = map(int, input().split())

card = list(map(int, input().split()))

value = 0
answer = []
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            cnt = card[i]+card[j]+card[k]
            if cnt <= M:
                if value < cnt :
                    value = cnt
                    answer = [card[i],card[j],card[k]]
print(sum(answer))