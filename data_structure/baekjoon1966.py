import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# enumerate : 원소와 인덱스를 한 쌍으로(0,A),(1,B)... 묶어서 줌(튜플)
queue = deque(enumerate(map(int, input().split()), start=1))
answer = []
while queue:
    idx, paper = queue.popleft()
    answer.append(idx)

    if paper > 0 :
        queue.rotate(-(paper-1))
    elif paper < 0 :
        queue.rotate(-paper)
print(' '.join(map(str, answer)))    

