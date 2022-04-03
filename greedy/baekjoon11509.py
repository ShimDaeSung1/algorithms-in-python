import sys
input = sys.stdin.readline

N = int(input())
h = list(map(int,input().split()))



# 높이별 화살 갯수, 0층 ~ N층 까지 있기 때문에 N+1개 / 1층에 풍선 있을 경우 1층 풍선 맞으면 화살은 0층으로 떨어짐
cnt = [0]*1000001

for i in h:
    if cnt[i] > 0 :
        cnt[i] -= 1
        cnt[i-1] += 1
    elif cnt[i] ==0:
        cnt[i-1] += 1
    else:
        print('-1')
        sys.exit()
print(sum(cnt))


