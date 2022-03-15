import sys
input = sys.stdin.readline

N, L = map(int,input().split())
location = list(map(int,input().split()))
location.sort()

tape = 0
if N>0 :
    tape = 1

start = location[0]
end = start + L - 0.5

for i in location:
    if end > i:
        continue
    else :
        tape+=1
        end = i+L-0.5
print(tape)

