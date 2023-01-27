import sys
input = sys.stdin.readline

#나무의 수, 집으로 가져가려고 하는 나무의 길이
n, m = map(int, input().split())

# 트리 개수는 100만까지
trees = list(map(int, input().split()))

# 이분탐색 검색 범위 설정
start = 1
end = max(trees)


while start <= end :
    # 트리 높이 중앙값
    mid = (start+end)//2

    log = 0
    for i in trees:
        if i >= mid:
            log += i-mid

    if log >= m:
        start = mid+1
    else :
        end = mid-1

print(end)







    
    

