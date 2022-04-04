import sys
input = sys.stdin.readline

# 일의 개수 N <=1000 제한시간 1초, O(N^2)가능 (1000^2 = 100만)
N = int(input())

# T_i(완성될 때 필요한 시간)와 S_i(끝내야하는 시간)
work = [list(map(int, input().split()))for _ in range(N)]
work.sort(key=lambda x : (x[1]))

total_time = 0
min_rest = float('inf') #양의 무한대
for time, limit in work:
    total_time += time #지금까지 일 하는데 걸리는 시간의 합, 일이 끝나자마자 바로 일들을 시작해서,
    #  다 더한 값들이 각각의 limit보다 크면 -1, 작으면 허용, 하지만 limit에서 일 하는데 걸린 시간의 합을 빼주면
    # 최대한으로 쉴 수 있는 시간이 나온다. 그 값들 중 가장 작은값에 맞춰야 나머지 일도 진행할 수 있다.
    min_rest = min(min_rest, limit-total_time) #제한시간-걸린시간
    if total_time > limit:
        print(-1)
        sys.exit()
print(min_rest)

# 일들이 바로 진행이라고 가정
# 3 <= 5  : 2시간 휴식 가능
# 3+8<=14 : 3시간 휴식 가능
# 3+8+1<=16 : 4시간 휴식 가능
# 3+8+1+5<=20 : 3시간 휴식 가능
# 이 중 하나라도 성립이 안 되면 일 할 수 없는 것
# 4시간 휴식 하게되면 3+8+1<=16을 제외한 나머지 일을 진행할 수 없다.
# 가장 최소인 2시간 휴식을 해야 나머지 일도 진행 가능





