#1343
import sys
input = sys.stdin.readline

X = input()
X = X.replace("XXXX", "AAAA") #replace(old, new, [count]) count는 변경할 횟수로, 입력하지 않으면 old의 문자열 전체를 변경한다. 앞에서부터 바뀐다.
X = X.replace("XX", "BB")

if X.count('X') >= 1:
  X = -1
print(X)