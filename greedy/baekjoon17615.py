import sys
input = sys.stdin.readline

N = int(input())
balls = input().strip()

count_list = []

# 맨 왼쪽에 있는 R 뭉텅이 제거 후 모든 R을 왼쪽으로 옮기는 케이스
parse_ball = balls.lstrip('R')
count_list.append(parse_ball.count('R'))

# 맨 오른쪽에 있는 R 뭉텅이 제거 후 모든 R을 오른쪽으로 옮기는 케이스
parse_ball = balls.rstrip('R')
count_list.append(parse_ball.count('R'))

# 맨 왼쪽에 있는 B 뭉텅이 제거 후 모든 B를 왼쪽으로 옮기는 경우
parse_ball = balls.lstrip('B')
count_list.append(parse_ball.count('B'))

# 맨 오른쪽에 있는 B 뭉텅이 제거 후 모든 B를 오른쪽으로 옮기는 경우
parse_ball = balls.rstrip('B')
count_list.append(parse_ball.count('B'))

print(min(count_list))
