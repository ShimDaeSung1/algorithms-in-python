import sys
input = sys.stdin.readline

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):
        if word[index] != word[index+1]: #연달아 있는 문자 두개가 다를 때
            new_word = word[index+1:] #현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index])>0: #남은 문자열에서 현재글자가 있다면
                error += 1
    if error == 0:
        group_word += 1
print(group_word)
