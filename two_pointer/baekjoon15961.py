import sys
input = sys.stdin.readline
from collections import defaultdict

#접시의 수, 초밥의 가짓 수, 연속해서 먹는 접시의 수, 쿠폰 번호
n, d, k, c = map(int, input().split())
dishies = []
dict_ = defaultdict(int)

for _ in range(n):
    dishies.append(int(input()))

for i in range(k): #0부터 k까지 슬라이딩 윈도우
    dict_[dishies[i]] += 1
dict_[c] += 1

left = 0
right = k-1
answer = 0
while left < n-1:
    dict_[dishies[left]] -= 1
    dict_[c] += 1#쿠폰 항상 먹기
    if dict_[dishies[left]] == 0 :
        del dict_[dishies[left]]

    left += 1
    right += 1

    if right >= n :
        right = 0 
    dict_[dishies[right]] += 1

    answer = max(answer, len(dict_))
    print(dict_)
print(answer)
        
    
