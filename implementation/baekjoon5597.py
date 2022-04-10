import sys
input = sys.stdin.readline

student = [i for i in range(1, 31)]
M = 28

for i in range(M):
    submit = int(input())
    # pop은 특정 인덱스, remove는 특정 값 제거 가능
    student.remove(submit)
student.sort()
for i in range(len(student)):
    print(student[i])
