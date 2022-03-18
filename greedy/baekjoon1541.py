import sys
input = sys.stdin.readline

# calc = str(input())

# # "-"로 분리해서 각각의 문자열을 리스트에 할당
# calc_backminus = calc.split("-")

# arr = []
# for i in calc_backminus:
#     # eval은 수식이 들어간 string을 int로 변환해줌
#     arr.append(eval(i))

# sum = 0
# for i in range(len(arr)):
#     if i%2 == 0:
#         sum+=arr[i]
#     else:
#         sum-=arr[i]
# print(sum)

arr = input().split('-')
sum = 0

for i in arr[0].split('+'):
    sum+=int(i)
for i in arr[1:].split('+'):
    sum-=int(i)

print(sum)



