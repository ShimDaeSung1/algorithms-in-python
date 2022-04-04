# import sys
# input = sys.stdin.readline

# # N자리 숫자 K개를 지워서 얻을 수 있는 가장 큰 수 구하기
# N, K = map(int, input().split())
# arr = input()
# arr_int = []
# for i in range(N):
#     arr_int.append(int(arr[i]))

# answer = []
# index = 0
# plus = N-(N-K)+1

# while len(answer) < N-K  :
#     answer.append(max(arr_int[index:plus]))
#     index = arr_int.index(max(arr_int[index:plus]))
#     print(index, plus)
#     arr_int[index] = 0
#     index += 1
#     plus += 1
    
# # 숫자로된 리스트를 문자열로 변환
# print(''.join(map(str,answer)))



# 스택으로 풀이
N, K = map(int, input().split())
num = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])

print(''.join(stack[:N-K]))
