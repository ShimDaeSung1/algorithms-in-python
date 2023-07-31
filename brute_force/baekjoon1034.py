import sys
input = sys.stdin.readline

n,m = map(int, input().split())
answer = 0
lamps = []

for _ in range(n):
    lamp = input().strip()
    lamp = list(map(int, lamp))
    lamps.append(lamp)

k = int(input())

for i in range(n):
    #같은 행 개수
    temp_answer = 0
    cnt_zero = lamps[i].count(0)
    #0이 k개 이하면서 k와 짝수/홀수를 맞춰야함
    if cnt_zero <= k and (k%2 == cnt_zero%2):
        temp_answer += 1
        for j in range(n):
            if i == j : continue
            if lamps[i] == lamps[j] :
                temp_answer += 1
        answer = max(answer, temp_answer) 

print(answer)
