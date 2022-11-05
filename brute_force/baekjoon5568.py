from itertools import permutations
import sys
input = sys.stdin.readline

#카드 n장
n = int(input())
#카드 k장 뽑기
k = int(input())

card_cnt = []
for _ in range(n):
    card_cnt.append(int(input()))

card_mixed = permutations(card_cnt, k)
arr = []
answer = set()
for i in card_mixed:
    cnt = ""
    for j in i:
        cnt += str(j)
    answer.add(cnt)
print(len(answer))
