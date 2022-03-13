def solution():
    n, k = map(int, input().split())
    #K개의 바구니에 들어있는 공의 개수가 1개 이상이며 전부 달라야 하기 때문에 공의 최솟값은k(k+1)/2
    #그리고 공의 합은 n보다 크면 안 된다.
    sum_minimum = k*(k+1)//2
    if sum_minimum > n:
        return -1
    if (n-sum_minimum) % k == 0:
        return k-1
    else:
        return k
print(solution())