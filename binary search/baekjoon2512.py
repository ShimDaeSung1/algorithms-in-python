import sys
input = sys.stdin.readline

# 정부의 예산 분배

#지방의 수
n = int(input())
# 각 지방에서 요청한 돈
request = list(map(int, input().split()))
# 예산
money = int(input())

start = 1
end = money
answer = float("-inf")

# 다 더해도 예산 아래일 경우
if sum(request) <= money:
    print(max(request))
    exit()

while start <= end:
    middle = (start+end)//2
    #줄 수 있는 돈
    can_give = 0

    for i in request:
        can_give += min(middle, i)
    #  예산보다 큰 돈을 써야할 경우 => 낮춰야함
    if can_give > money:
        end = middle-1
    # 예산보다 작거나 같을 경우, 단 모든요청 금액을 다 더해도 예산보다 작을 경우엔
    # 항상 can_give가 예산보다 작다. 그래서 while문 전에 걸러줘야함
    elif can_give <= money : 
        answer = max(middle, answer)
        start = middle+1
print(answer)
    

    
    
