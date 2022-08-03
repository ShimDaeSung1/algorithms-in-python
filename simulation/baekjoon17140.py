from collections import Counter
import sys
input = lambda:sys.stdin.readline().strip()

def rc():
    max_len = 0
    len_s = len(s)
    for j in range(len_s):
        a = [i for i in s[j] if i != 0]
        # Counter : 데이터의 개수 출력 / most_common() : 데이터의 개수가 많은 순으로 정렬된 배열 리턴
        a = Counter(a).most_common()
        a.sort(key = lambda x : (x[1], x[0]))
        s[j] = []
        for fi, se in a:
            s[j].append(fi)
            s[j].append(se)
        len_a = len(a)
        # 크기가 가장 큰 행 구해서 나머지 행의 뒤에 0을 붙여야 하므로
        # a는 (2,1),(1,2) 이런 식이므로 전체 길이 * 2
        if max_len < len_a*2 : max_len = len_a * 2
    for j in range(len_s):
        for k in range(max_len - len(s[j])):
            s[j].append(0)
        # 모든 행(열) 100열(행) 까지 잘라줌
        s[j] = s[j][:100]

r, c, k = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(3)]
for i in range(101):
    try: # 처음엔 무조건 3행 3열인데, r과 c가 3초과 일 수도 있으므로 일단 예외처리
        if s[r-1][c-1] == k:
            print(i)
            break
    except:pass
    # 행 < 열 : 열에 대한 연산이므로 zip함수로 행과 열을 바꾼다.
    if len(s) < len(s[0]):
        # zip은 지퍼처럼 양쪽으로 올리듯이 모든 배열에서 하나씩 뽑아서 연결해준다.
        # 즉 zip을 하면 각 행에서 1번 열씩 뽑아서 행으로 만들기 때문에,
        # 열과 행이 바뀐다.
        s = list(zip(*s))
        rc()
        s = list(zip(*s))
    else:
        rc()
# for-else : for문이 중간에 break 등으로 끊기지 않고, 끝까지 수행 되었을 때 수행하는 코드
else:
    print(-1)
         

