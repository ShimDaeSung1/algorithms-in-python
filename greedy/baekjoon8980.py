import sys
input = sys.stdin.readline

# 마을 수N과 트럭 용량 C
N, C = map(int, input().split())
# 보내는 박스 정보의 개수 M
M = int(input())

pickup = [list(map(int, input().split()))for _ in range(M)]
pickup.sort(key = lambda x : (x[1]))

answer = 0 # 최대 박스 수
remain = [C]*(N+1) #각 위치에 남은 공간(트럭 안에)

for i in range(M):
    temp = C # C개를 옮길 수 있다고 가정
    # 항상 도착지에서 배송을 끝마친 상태라 temp는 C가 된다.
    for j in range(pickup[i][0], pickup[i][1]):
        # 배달 도착 전까지 갖고 움직일 수 있는 최소한의 개수를 움직인다.        
        # 각 지점에서 트럭 안에 남아있는 개수와 총 용량과의 최솟값을 비교한다.(작은 값을 모든 지점에서 움직일 수 있다.)
        temp = min(temp, remain[j])
    # 각 지점에서 트럭 안의 남은 용량과 총 용량의 작은 값과 현 지점에서 옮겨야하는 최대 박스 개수의 최솟값을 움직인다.
    temp = min(temp, pickup[i][2])
    for j in range(pickup[i][0], pickup[i][1]):
        # 배달 지점 전까지의 모든 지점에서의 트럭의 용량에 temp의 값을 빼줘야 가져갈 수 있는 남은 용량이 표시된다. 
        remain[j] -= temp
    answer += temp
print(answer)
    


    

