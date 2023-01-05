import sys
input = sys.stdin.readline

n = int(input())

water = list(map(int, input().split()))
water.sort()

left = 0
right = n-1
answer = abs(water[left]+water[right])
final = [water[left], water[right]]

while left < right :
    sum = water[left] + water[right]

    if abs(sum) < answer:
        answer  = abs(sum)
        final = [water[left], water[right]]
        if answer == 0 :
            break
    if sum < 0:
        left += 1
    else:
        right -= 1
    
print(*final)



