import sys
input = sys.stdin.readline

N = int(input())
item = list(map(int, input().split()))
item.sort()

arr_side = []

if len(item)%2 ==0:
    for i in range(len(item)//2,len(item)):
        arr_side.append(item[i]*2)
    # data = item[((len(item)//2))]
    # arr_avg = data*len(item)
    # print(max(arr_avg,sum(arr_side),sum(item)))
    print(sum(arr_side))
else :
    for i in range((len(item)//2)+1,len(item)):
        arr_side.append(item[i]*2)
    arr_side.append(item[(len(item)//2)])
    # data = item[((len(item)//2))]
    # arr_avg = data*len(item)
    # print(max(arr_avg,sum(arr_side),sum(item)))
    print(sum(arr_side))




    # A = int(item[1]*3)
    # for i in range(3+((len(item)-3)//2), len(item)):
    #     arr_side.append(item[i]*2)
    # arr_side.append(A)
    # data = item[(((len(item)+1)//2)-1)]
    # arr_avg = data*len(item)
    # print(max(arr_avg,sum(arr_side),sum(item)))





