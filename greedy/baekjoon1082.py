import sys
input = sys.stdin.readline

# 가장 큰 숫자를 만들기 위해서는 최대한 많은 자릿수를 확보한다.
# 그 후 가장 큰 자릿수부터 큰 숫자로 바꿀 수 있는지 남은돈과 바꿀때 드는 차액을 비교한다.

# 예외
# 0이 가장 싼 경우, 시작 숫자가 0000이 된다. => 0을 다시 환불하고 돈을 받아 0이외의 숫자 구매
# 0을 다 팔았는데도 다른 숫자를 살 수 없으면 답이 0
N=int(input())
L = list(map(int,input().split()))
money = int(input())

minCost = min(L)
minNum = L.index(minCost)

if N == 1:
    print(0)
    sys.exit()

def add(remainMoney, digit):
    # 가장 큰(index가 큰) 오른쪽 숫자부터 넣어보기
    for i in range(digit, -1, -1):
        # 만약 pick[i]이 L에서 가장 큰 인덱스를 가져온 경우가 아니라면, 즉 더 큰걸로 바꿀 수 있는 가능성이 있다면
        if pick[i]!=N-1:
            # 큰거부터 넣어본다
            for j in range(N-1, pick[i], -1):
                nowCost = L[j]-L[pick[i]]
                if nowCost <= remainMoney:
                    pick[i]=j
                    add(remainMoney-nowCost, digit-1)
                    return
    # 모두 다 0이면
    # any는 하나라도 True면 True
    if not any(pick):
        # 0을 다 팔았는데도 다른 숫자를 살 수 없는 경우 0 출력
        if not pick:
            print(0)
            sys.exit()
        pick.pop()
        add(remainMoney+L[0], digit-1)

            

num = money // minCost
pick = [minNum for _ in range(num)]
cost = num*minCost
add(money-cost, num-1)
ans = 0
for i in range(len(pick)):
    # pick=[a,b,c,d] => [0,0,1,2]일 경우 2*1000+1*100+b*10+a*1을 의미
    ans += (10**i)*pick[i]
print(ans)
