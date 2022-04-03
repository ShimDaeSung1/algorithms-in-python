import sys
input = sys.stdin.readline
# 시간 제한은 1초이고, 보통 1억 정도의 값이 1초이므로
# O(N):약 1억
# O(N^2):약1만
# O(N^3):약500
# O(2^N):약20
# O(N!):10
# 단순 for문은 O(N)이므로 N이 1억일 때 까지 가능, 이중for문은 O(N^2)이므로 N이 1만 이내
# 만약 O(N^2)의 시간 복잡도에 N이 10만까지 주어질 경우, 값은 100억으로, 100초가 걸림

# 해당 문제는 1초이다.
# 해당 문제의 N의 입력 크기는 300,000이다.
# 문제에서 주어진 시간과 입력N의 크기를 곱하면 1*300,000 = 300,000



# 원생의 수 N , 나누려고 하는 조의 개수 K
N, K = map(int, input().split())
height = list(map(int, input().split()))

# 인접한 사람들의 키를 모두 arr에 저장 후
arr = []
for i in range(N-1):
    arr.append(height[i+1]-height[i])
arr.sort()
# 큰 순서부터 K-1만큼 연결을 끊어주면 된다

for i in range(K-1):
    # pop은 마지막 원소를 뽑는다
    arr.pop()
print(sum(arr))

