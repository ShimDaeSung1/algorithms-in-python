import sys
input = sys.stdin.readline

A = input()
B = input()

#B의 뒤에서부터 세는데, A의 뒤에서 하나씩 번갈아가면서 B의 고정된 위치의 값 한 개와
#비교한 후, 같은 값들은 놔두고(위치는 달라도 됨) 서로 다른 값의 알파벳들만 옮기기 때문에
#총 길이 - (B의 뒤에서부터 위치는 다르지만 A와 동일한 알파벳의 수)

ans = len(A)
idx = len(A) - 1

for i in range(idx,-1,-1):   
    if A[i] == B[idx]:
        ans-=1
        idx-=1

A = sorted(A)
B = sorted(B)

ans_1 = 0
for i in range(len(A)):
    if A[i] != B[i]:
        ans_1 = -1
        print(ans_1)
        break
if ans_1 == 0:
    print(ans)
