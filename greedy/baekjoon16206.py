import sys
input = sys.stdin.readline
#롤케이크 갯수 N과 자를 수 있는 최대 횟수 M
N, M = map(int,input().split())

cakes = list(map(int,input().split()))
# 작은 것부터 차례대로 자르는데, 이는 10, 20이 있다면 먼저 잘라줘야 적은 횟수로 잘라내기 때문
# 10의 배수를 먼저 잘라줘야 더 많은 케이크를 얻을 수 있다.
# 23은 1번 자르면 10과 13, 즉 먹을 수 있는 케이크가 1개지만
# 20은 1번 자르면 10과 10, 먹을 수 있는 케이크가 두개가 되므로 10의 배수를 먼저 자른다.
cakes.sort(key=lambda x : ((x%10),x))
# x를 10으로 나누어 나머지가 작은 순서대로 출력하는데, 같으면(10, 20) x의 값을 기준으로 오름차순 정렬

count = 0

for cake in cakes :
    if M > 0 :
        if cake < 10 :
            continue
        elif cake == 10 :
            count+=1
            continue
        else: 
            if cake % 10 == 0  :
                cnt = (cake // 10)-1
                if cnt > M :
                    cnt = M
                    if cake == 20:
                        count += cnt+1
                    else:
                        count += cnt
                    M=0
                    continue
                else :
                    count += cnt+1
                    M -= cnt
                    continue
            else:
                cnt = cake // 10
                if cnt > M:
                    cnt = M
                    count += cnt
                    M -= cnt
                    continue
                else:
                    count += cnt
                    M -= cnt
                    continue
    else:
        break
print(count)


