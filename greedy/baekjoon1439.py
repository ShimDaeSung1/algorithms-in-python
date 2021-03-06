# 001100, 00011000011 등 이것은 각각 010, 0101로 볼 수 있다.
# 길이에 상관없이 문자만 바뀌면 되는지 보기만 하면 되므로

# 숫자 > 변화 횟수 > 뒤집어야 할 횟수 
# 01 > 1 > 1
# 010 > 2 > 1
# 0101 > 3 > 2
# 01010 > 4 > 2
# 010101 > 5 > 3
# 즉, 변화횟수 + 1 한 후 2로 나눈 몫만 가져오면 됨

import sys
input = sys.stdin.readline

S = input()
count = 0
for i in range(len(S)-2):
    if S[i] != S[i+1]:
        count += 1
print((count + 1) // 2)