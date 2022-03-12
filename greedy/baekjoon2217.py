import sys
input = sys.stdin.readline
#2217
N = int(input())
rope = []

for i in range(0,N):
  rope.append(int(input()))
rope.sort(reverse=True)

max_value = []
for i in range(N):
  max_value.append(rope[i]*(i+1))

print(max(max_value))


