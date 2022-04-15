import sys
input = sys.stdin.readline

arr = []
def draw(index):
    if index == 0 and visited[index] == True:
        for i in range(index, len(visited)-1):
            arr.append('*')
        return print(''.join(arr))
    elif index >= 1 and visited[index] == False:
        for i in range(index, len(visited)-1-index):
            arr[i] = ' '
        return print(''.join(arr))
    elif index >= 1 and visited[index] == True:
        for i in range(index, len(visited)-1-index):
            arr[i] = '*'
        return print(''.join(arr))

def draw_2(index):
    if index % 2 == 1 and visited[index+1] == True:
        for i in range(len(visited)-2-index, index+1):
            arr[i] = ' '
        return print(''.join(arr))
    elif index % 2 == 0 and visited[index] == True:
        for i in range(len(visited)-1-index, index):
            arr[i] = '*'
        return print(''.join(arr))



N = int(input())
count = 0
if N == 1 :
    count = 1
else:
    count = 1
    count+=(N-1)*4

visited = [True] * (count+1)
for i in range(len(visited)):
    if i%2==1 : 
        visited[i] = False

for i in range(count):
    if i >= count//2 + 1:
        draw_2(i)
    else : 
        draw(i)
