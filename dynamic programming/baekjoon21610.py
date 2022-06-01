n = int(input())
count = 0

# 우선 5로 나눠서 되는지 확인, 아니면 3씩 빼줘서 5로 나눠질 때 까지 
while n >= 0 :
    if n % 5 == 0:
        count += n//5
        print(count)
        break
    n -= 3
    count += 1
# 빠져나왔음에도 while의 조건식이 false인 경우 (n<0)
else:
    print(-1)


