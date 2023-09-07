import sys
input = sys.stdin.readline

# n은 10만
n = int(input())

lst = list(map(int, input().split()))

answer = float("inf")
left = 0
right = n-1

while left < right:
    temp_ans = lst[left]+lst[right]
    
    if temp_ans > 0 :
        right -= 1
    elif temp_ans < 0 :
        left += 1
    else :
        answer = 0
        break
        
    a = abs(temp_ans)
    if a < abs(answer):
        answer = temp_ans

# left = 0
# right = n-1
# while left < right : 
#     temp_ans = lst[left]+lst[right]
    
#     if temp_ans > 0 :
#         left += 1
#     elif temp_ans < 0 :
#         right -= 1
#     else : 
#         answer = 0
#         break
    
#     a = abs(temp_ans)
#     if a < abs(answer):
#         answer = temp_ans

print(answer)
