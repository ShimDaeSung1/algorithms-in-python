import sys
input = sys.stdin.readline

# 시작 높이
N = int(input())
#5

# 풍선의 높이
H = list(map(int, input().split()))
# 2 1 5 4 3

arr = [[int(0) for col in range(5)] for row in range(5)]

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end= ' ')
#     print()


for i in range(len(H)):

    arr[len(H)-H[i]][i] = H[i]


for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end= ' ')
    print()

arrow = 1

for i in range(5-N, -1):
    for j in range(len(arr[i])):
        if arr[i][j]>0:
            arr[i][j]=0
            # 0으로 바꿔준 후 j는 그대로, i는 하나 내려주고 돌아야함, 작성
            break
    
print(arrow)