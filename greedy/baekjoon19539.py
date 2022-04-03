import sys
input = sys.stdin.readline

# 이하가 뒷뜰에 심은 사과나무 개수
N = int(input())
# 바라는 나무의 높이
arr = list(map(int, input().split()))
arr_sum = sum(arr)
data = arr_sum//3 # 몫 

if sum(arr)%3 != 0 : #3으로 나누어 떨어져야함
    print("NO")
else: # 2와 1을 쓴 개수는 서로 동일
    for a in arr:
        data -= a//2 
    if data > 0 : #2로 나눈 몫이 3으로 나눈 몫보다 크거나 같아야함
        print("NO")
    else :
        print("YES")



    

    
    



