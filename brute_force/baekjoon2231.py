import sys
input = sys.stdin.readline

value = int(input())

min_value = 1000001

for i in range(1,value):
    i_list = list(map(int, str(i)))
    a = i+sum(i_list)
    if a == value :
        min_value = min(i, min_value)
if min_value == 1000001:
    print(0)
else:
    print(min_value)
