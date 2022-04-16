# import sys
# input = sys.stdin.readline


# def check(number):
#     copy_num = number-1
#     i = 1

#     while copy_num-i >= 0 and copy_num+i < len(switch):
#         if switch[copy_num-i] == switch[copy_num+i]:
#             switch[copy_num-i] = switch[copy_num-i]^1
#             switch[copy_num+i] = switch[copy_num+i]^1
#             i += 1
#         else:
#             break
#     # return i




# N = int(input())
# switch = list(map(int, input().split()))

# # 학생 수
# st = int(input())
# for i in range(st):
#     gender, number = map(int, input().split())
#     copy_number = number
#     if gender == 1 :
#         while copy_number <= len(switch):
#             if copy_number == 1:
#                 # 두 비트가 다를 때 1 --> (1,1):0 / (0,0):0 / (1,0):1 / (0,1):1
#                 # 0이면 1로, 1이면 0으로 변환 xor비트연산자
#                 for d in range(len(switch)):
#                     switch[d] = switch[d]^1
#                 break
#             else: 
#                 switch[copy_number-1] = switch[copy_number-1]^1
#                 copy_number += number
#     else:
#         switch[number-1] = switch[number-1]^1
#         check(number)


# for i in range(len(switch)):
#     print(switch[i], end=' ')
#     if i == 19:
#         print()
#         continue
#     if i>20 and i%20 == 0 :
#         print()

def change(num):
    switch[num] = switch[num]^1

N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N):
            if num + k > N or num - k < 1 : break
            if switch[num+k] == switch[num-k]:
                change(num+k)
                change(num-k)
            else:
                break
for i in range(1, N+1):
    print(switch[i],end=' ')
    if i %20 == 0 :
        print()


            
