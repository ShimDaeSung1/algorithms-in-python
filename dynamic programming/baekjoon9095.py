t = int(input())

# def answer(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     else:
#         return answer(n-1)+answer(n-2)+answer(n-3)

# for i in range(t):
#     n = int(input())
#     print(answer(n))
for i in range(t):
    n = int(input())
    dp = [0,1,2,4]
    for j in range(4, n+1):
        dp.append(dp[j-1]+dp[j-2]+dp[j-3])
    print(dp[n])
    

