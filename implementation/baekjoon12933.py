import sys
input = sys.stdin.readline

duck = input().rstrip()
if len(duck) % 5 != 0 :
    print(-1)
    sys.exit()

count = 0
visited = [False] * len(duck)

def start(index):
    global count
    quack = "quack"
    j = 0
    first = True
    for i in range(index, len(duck)):
        if duck[i] == quack[j] and visited[i] == False:
            visited[i] = True
            j += 1
            if duck[i] == 'k':
                if first == True:
                    count += 1
                    first = False
                j = 0
                continue
                

    
for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        start(i)


if count == 0 or not all(visited):
    print(-1)
else:
    print(count)
