import sys
input = sys.stdin.readline

# 센서의 개수
N = int(input())

# 집중국의 개수
K = int(input())

if K >= N:
    print(0)
    sys.exit()
    
# N개 센서 좌표
location = list(map(int, input().split()))
location.sort()
per_len = []
for i in range(N-1):
    per_len.append(location[i+1]-location[i])

per_len.sort()

for i in range(K-1):
    per_len.pop()
print(sum(per_len))