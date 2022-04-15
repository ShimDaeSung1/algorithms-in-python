import sys
input = sys.stdin.readline

L, R = input().split()
li = list(input().rstrip())

keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']
location = dict()

for x in range(3):
    for y in range(len(keyboard[x])):
        location[keyboard[x][y]] = (x,y)

Lx, Ly = location[L]
Rx, Ry = location[R]
answer = 0

L_str = "qwertasdfgzxcv"

for s in li:
    if s in L_str:
        sx, sy = location[s]
        answer += 1+ abs(Lx-sx)+abs(Ly-sy)
        Lx, Ly = sx, sy
    else:
        sx, sy = location[s]
        answer += 1+ abs(Rx-sx)+abs(Ry-sy)
        Rx, Ry = sx, sy
print(answer)

