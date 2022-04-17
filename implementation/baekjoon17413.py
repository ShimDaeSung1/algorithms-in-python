import sys
input = sys.stdin.readline

def check_alphaNum(index):
    str = []
    for i in range(index, len(li)):
        if li[i] == ' ' and visited[i] == False:
            break
        if li[i] == '<' and visited[i] == False :
            break
        if visited[i] == False:
            str.insert(0, li[i])
            visited[i] = True
    answer.append(str)


def check_special(index):
    str = []
    for i in range(index, len(li)):
        if li[i] == '>' and visited[i] == False:
            visited[i] = True
            str.append(li[i])
            break
        str.append(li[i])
        visited[i] = True
    answer.append(str)



li = input().rstrip()
visited = [False]*len(li)
answer=[]

for i in range(len(li)):
    if li[i] == '<' and visited[i] == False:
        check_special(i)
    elif li[i] == ' ' and visited[i] == False:
        visited[i] = True
        answer.append(' ')
    else :
        if visited[i] == False: 
            check_alphaNum(i)
for i in answer:
    for j in i:
        print(j,end='')


