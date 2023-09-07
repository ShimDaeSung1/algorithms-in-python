import sys
input = sys.stdin.readline

# n개의 숫자중 합이 S이상인 가장 짧은 연속 부분합중 최소 길이 구하기
n,s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = float("inf")
max_length = len(numbers)
left, right = 0, 0

recent = numbers[0]

while left < max_length:
    # 합이 s 이상이면 줄여도됨
    if recent >= s:
        recent -= numbers[left]
        answer = min(answer, right-left+1)
        left += 1
    # 합이 s 보다 작으므로 한칸 늘리기
    else:
        if right == max_length-1:
            #오른쪽이 맨 끝이므로 다음은 볼 필요 없음
            break
        right += 1
        recent += numbers[right]
if answer == float("inf"):
    print(0)
    exit()
print(answer)
    
