import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
total = []
ans = 0
day = 0
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
# 5
# 1 3 2 4 6
# 2 7 3 4 1
for i in range(n):
    total.append([arr[i],arr2[i]])
# total = [(1, 2), (3, 7), (2, 3), (4, 4), (6, 1)]

#비교할 아이템이 요소가 복수 개일 경우, 튜플로 우선순위를 정해줄 수 있다.
#-를 붙이면 현재와 반대차순으로 정렬된다.
#a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]
#e = sorted(a, key = lambda x : (x[0], -x[1])) 
#  => [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]
total.sort(key = lambda x : (x[1], -x[0]))
#total = [(6, 1), (1, 2), (2, 3), (4, 4), (3, 7)]

for i in range(n):
    ans += total[i][0] + total[i][1] * day
    day += 1
print(ans)
