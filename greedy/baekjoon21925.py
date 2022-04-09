import sys
input = sys.stdin.readline

def check(idx, cnt):
    global result
    if idx == N:
        print(cnt)
        result = max(result, cnt)
        exit()
        return
    else:
        # 0과 1, 0과 3, 0과 5, 0과 7 이런식으로 묶어서 True면 cnt를 1 올리고 next_idx+1 부터 다시 돌린다
        for next_idx in range(idx+1, N, 2):
            if dp[idx][next_idx]:
                check(next_idx+1, cnt+1)


N = int(input())
arr = list(map(int, input().split()))

dp = [[True if i == j else False for j in range(N)] for i in range(N)]
for i in range(N-1):
    if arr[i] == arr[i+1]:
        # arr에서 인덱스가 가깝게 붙어있는 ex)1,2가 같다면 1행 2열을 True로 만듦
        dp[i][i+1] = True

# 붙어있는 애들을 해줬으니 2칸 이상 ~ 끝까지 비교
for i in range(2, N):
    for j in range(N-i):
        # 그 위치보다 2~N-1칸 떨어진 숫자들을 다 비교 후 ex) arr[4], arr[4+3]의 값이 같고 dp[5][6]이 같다면 arr[4],arr[4+3]과 arr[5],arr[6]이 서로 대칭이므로 팰린드롬 성립 
        if arr[j] == arr[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i] = True

max_num = N//2
result = -1
check(0,0)
print(result)

