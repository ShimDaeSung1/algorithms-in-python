import sys
input = sys.stdin.readline

n = 0
dic = dict()
while True:
    str = input().rstrip()

    if not str:
        break

    if str in dic.keys():
        dic[str] += 1
    else:
        dic[str] = 1
    n+=1

tree_list = list(dic.keys())
tree_list.sort()

for i in tree_list:
    print('%s %.4f' %(i, dic[i]/n*100))

