import sys
input = sys.stdin.readline


def check(number):
    copy_num = number-1
    i = 1

    while copy_num-i >= 0 and copy_num+i < len(switch):
        if switch[copy_num-i] == switch[copy_num+i]:
            switch[copy_num-i] = switch[copy_num-i]^1
            switch[copy_num+i] = switch[copy_num+i]^1
            i += 1
        else:
            break
    # return i




N = int(input())
switch = list(map(int, input().split()))

# 학생 수
st = int(input())
boy = 1
girl = 2
for i in range(st):
    gender, number = map(int, input().split())
    copy_number = number
    if gender == boy :
        while copy_number <= len(switch):
            if copy_number == 1:
                # 두 비트가 다를 때 1 --> (1,1):0 / (0,0):0 / (1,0):1 / (0,1):1
                # 0이면 1로, 1이면 0으로 변환 xor비트연산자
                for d in range(len(switch)):
                    switch[d] = switch[d]^1
                break
            else: 
                switch[copy_number-1] = switch[copy_number-1]^1
                copy_number += number
    else:
        switch[number-1] = switch[number-1]^1
        check(number)


for i in range(len(switch)):
    print(switch[i], end=' ')


            
