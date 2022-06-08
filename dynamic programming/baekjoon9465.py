t = int(input())

dx = [-1, 1]
dy = [1, 1]

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    for j in range(1, n):
        if j == 1:
            arr[0][j] += arr[1][j-1]
            arr[1][j] += arr[0][j-1]
        else:
            arr[0][j] += max(arr[1][j-1], arr[1][j-2])
            arr[1][j] += max(arr[0][j-1], arr[0][j-2])
    print(max(arr[0][-1], arr[1][-1]))
    




    

    

