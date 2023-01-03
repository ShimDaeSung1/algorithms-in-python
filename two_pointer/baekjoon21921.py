import sys
input = sys.stdin.readline

# 블로그 시작한지 N일, X일동안 가장 많이 들어온 방문자 수 구하기
N, X = map(int, input().split())

visitors = list(map(int, input().split()))

max_visitors = 0
max_visitors_cnt = 0

visitor = sum(visitors[:X])
left = 0
right = X-1

while right < N:
    if max_visitors < visitor:
        max_visitors = visitor
        max_visitors_cnt = 1
    elif max_visitors == visitor:
        max_visitors_cnt += 1
    
    if right == N-1: break

    visitor -= visitors[left]
    left += 1
    right += 1
    visitor += visitors[right]

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(max_visitors_cnt)



