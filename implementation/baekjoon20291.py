import sys
input = sys.stdin.readline

N = int(input())
fileCount = dict()
arr = []
for i in range(N):
    file = input()
    index = 0
    for j in range(len(file)):
        if file[j] == '.':
            index = j
    key = file[index+1:]
    # 인덱스부터 끝까지 출력이므로 rstrip해서 공백 제거
    arr.append(key.rstrip())
    fileCount[key.rstrip()] = 0

for i in arr:
    if i in fileCount:
        # 딕셔너리의 키 값에 +1 해줌
        fileCount[i] = fileCount[i]+1
fileCount = sorted(fileCount.items())

for file, back in fileCount:
    print(file, back)



