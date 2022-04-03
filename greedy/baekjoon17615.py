import sys
input = sys.stdin.readline

N = int(input())
balls = input()

count_list = []

# 맨 왼쪽에 있는 R 하나 제거 후 모든 R을 왼쪽으로 옮기는 케이스
# parse_ball = balls.lstrip('R')
# count_list.append(parse_ball.count('R'))

# 맨 오른쪽에 있는 R 하나 제거 후 모든 R을 오른쪽으로 옮기는 케이스
parse_ball = balls.rstrip('R')
print(parse_ball)
