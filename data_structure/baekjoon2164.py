import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
cards = [i for i in range(1,n+1)]
cards.sort(reverse=True)
cards = deque(cards)

while len(cards)>1:
    cards.pop()
    cards.appendleft(cards.pop())
print(*cards)
