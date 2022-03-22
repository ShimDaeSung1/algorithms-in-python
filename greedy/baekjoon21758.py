import sys
input = sys.stdin.readline

#꿀통이 벌 사이에 있을 때
def bet_bee(honey, sum_honey):
    #벌은 양쪽 끝에 있어야 가장 많이 얻는다.
    return sum_honey[-2]-honey[0]+max(honey[1:-1])  

#꿀통이 양쪽 끝에 있을 때
def side_bee(honey, sum_honey):
    max_honey = 0
    #꿀통이 왼쪽 끝에 있는 경우, 맨 오른쪽에 벌을 하나 둔다
    for i in range(1, len(honey)-1):
        max_honey = max(max_honey, sum_honey[-2]+sum_honey[i-1]-honey[i])
    
    #꿀통이 오른쪽 끝에 있는 경우, 맨 왼쪽에 벌을 하나 둔다
    for i in range(1, len(honey)-1):
        max_honey = max(max_honey,sum_honey[-1]-honey[0]-honey[i]+sum_honey[-1]-sum_honey[i])
    return max_honey    

N = int(input())

honey = list(map(int, input().split()))

sum_honey = []
result = 0
for i in honey:
    result += i
    sum_honey.append(result)

print(max(bet_bee(honey, sum_honey),side_bee(honey, sum_honey)))

