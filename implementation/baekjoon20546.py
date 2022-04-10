import sys
input = sys.stdin.readline

money = int(input())
money_joon = money
money_seong = money
stock = list(map(int,input().split()))

# 준현이 매매법
cnt_joon = 0
for i in stock:
    if money_joon >= i:
        cnt_joon += money_joon//i
        money_joon -= i*(money_joon//i)
money_joon += cnt_joon*stock[-1]

# 성민이 매매법 3일 연속 상승 = 매도, 3일 연속 하락 = 매수
cnt_seong = 0
cnt_up = 0
cnt_down = 0
for i in range(1, len(stock)):
    if stock[i] > stock[i-1]:
        cnt_down = 0
        cnt_up += 1
    elif stock[i] < stock[i-1]:
        cnt_down += 1
        cnt_up = 0
    if cnt_down >= 3:
        if money_seong >= stock[i]:
            cnt_seong += money_seong//stock[i]
            money_seong -= stock[i]*(money_seong//stock[i])
    elif cnt_up == 3:
        money_seong += cnt_seong*stock[i]
        cnt_seong = 0
money_seong += cnt_seong * stock[-1]
  
if money_seong > money_joon:
    print("TIMING")
elif money_seong < money_joon:
    print("BNP")
else:
    print("SAMESAME")
