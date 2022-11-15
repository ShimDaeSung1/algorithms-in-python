import sys
input = sys.stdin.readline
dic = dict()

n, m = map(int, input().split())

for i in range(1, n+1):
    a = input().strip()
    dic[i] = a
    dic[a] = i

for i in range(m):
    quest = input().strip()
    if quest.isdigit():
        print(dic[(int(quest))])
    else:
        print(dic[quest])