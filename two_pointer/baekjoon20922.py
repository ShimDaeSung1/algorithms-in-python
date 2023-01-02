import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
# 포인터 두개
left, right = 0,0
# 각 숫자 반복 개수 저장
cnt = [0]*100001

while right < N:
    r_cnt = cnt[arr[right]]
    if r_cnt < K:
        cnt[arr[right]] += 1
        right += 1
    else:
        cnt[arr[left]] -= 1
        left += 1
    answer = max(answer, right-left)

print(answer)



