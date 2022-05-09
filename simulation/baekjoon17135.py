
from glob import glob
from heapq import heappop, heappush
from itertools import combinations
import sys
input = lambda:sys.stdin.readline().strip()

# 행의 수, 열의 수, 공격 거리 제한
n, m, d = map(int, input().split())

# 0은 빈 칸, 1은 적이 있는 칸
MAP = [list(map(int, input().split())) for _ in range(n)]
arr = []

castle_pos = [i for i in range(m)]
# combination(조합) : 서로 다른 n개 중에서 r개를 취하여 순서를 고려하지 않고
# (A,B)와 (B,A)를 같은 것으로 취급하여 나열한다.
# 궁수는 세명이고, 배치 시 나올 수 있는 경우의 수는 mC3 이므로 조합을 이용해서
# 궁수 3명을 배치하여 나올 수 있는 모든 경우를 구하고 잡을 수 있는 적들의 수 중
# 최대값을 구한다. 가장 가까운 적이 다수면 왼쪽 적 공격은 우선순위 큐로 구현
archer_cases = tuple(combinations(castle_pos,3))
answer = 0

# 직접 구현 (combinations)
# def combinations(array, r):
#     for i in range(len(array)):
#         if r == 1: # 종료조건
#             yield[array[i]] # 하나씩 꺼내서 나열, yield는 값을 리턴해주고 다시 함수로 돌아오게끔 한다.
#         else:
#             for next in combinations(array[i+1:], r-1):
#                 yield[array[i]] + next 
# for a in combinations(items, 3):
#     temp = copy.deepcopy(graph)

def get_enemy_count():
    global arr
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1: cnt += 1
    return cnt

def attack_enemy(archer_case_index):
    global arr
    remove_list = []
    attacked = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for archer_pos in archer_cases[archer_case_index]:
        pq = [] # [거리,x,y]를 우선순위 큐에 삽입

        for i in range(n-1, -1, -1):
            for j in range(m):
                if arr[i][j] == 1:
                    diff = abs(n-i) + abs(archer_pos-j)
                    if diff <= d:
                        # 왼쪽부터 잡아야하므로 열인 j가 두번째로 옴
                        heappush(pq, [diff, j, i])
        
        if pq:
            # 열인 j를 x로 받았으므로
            _, x, y = heappop(pq)
            # y와 x를 바꿔서 저장
            remove_list.append([y, x])
    for y, x in remove_list:
        if not attacked[y][x]:
            attacked[y][x] = True
            cnt += 1
            arr[y][x] = 0
    return cnt

def move_enemy():
    global arr
    arr[-1] = [0 for _ in range(m)]

    for i in range(-1, -n, -1):
        arr[i] = arr[i-1]
    arr[0] = [0 for _ in range(m)]

def simulation(archer_case_index):
    cnt = 0

    while get_enemy_count() != 0:
        cnt += attack_enemy(archer_case_index)
        move_enemy()
    
    return cnt

for i in range(len(archer_cases)):
    arr = [[MAP[i][j] for j in range(m)] for i in range(m)]
    cnt = simulation(i)
    if answer < cnt : answer = cnt
print(answer)






