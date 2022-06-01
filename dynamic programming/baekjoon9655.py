
n = int(input())
cnt = 0
while n > 0:
    if n % 3 == 0 :
        cnt += n//3 
        n = 0 
        break
    n -= 1
    cnt += 1
if cnt % 2 == 0:
    print("CY")
else:
    print("SK")
