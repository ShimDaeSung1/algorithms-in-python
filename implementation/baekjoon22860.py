import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)

direc = {} #폴더 딕셔너리, 키=밸류 direc=dict()
f_num = 0

def go(target, kinds):
    global f_num
    if target not in direc: #현재 탐색할 주체가 파일이나 폴더가 없다면 종료
        return
    
    for title, val in direc[target]:
        if val == 0: #파일이라면
            kinds.add(title)
            f_num += 1
        else: #폴더라면 더 탐색해서 들어간다
            go(title, kinds)




# main폴더 하위에 있는 폴더의 총 개수N, 파일 총 개수 M
n, m = map(int, input().split())

# 상위 폴더의 이름 P , 폴더 또는 파일의 이름F, 폴더or파일 C
for _ in range(n+m):
    From, To, Id = input().split()
    if From not in direc:
        direc[From] = []
        direc[From].append([To, int(Id)])
    else:
        direc[From].append([To, int(Id)])



# print(direc)

# for title in direc:
#     for key, value in direc[title]:
#         print(key, value)
q = int(input())

# s = set([1,2,3,4]) -> set
# s = {1,2,3,4} -> set
# s = {} ->dict
for i in range(q):
    query = input().split('/') #리스트 형태로 저장
    SET = set() #set은 집합자료형으로, 중복을 허용하지 않고 순서가 없다.
    f_num = 0
    #query의 맨 마지막 값과 집합자료형 들고 go
    go(query[-1], SET)

    print(len(SET), f_num)
