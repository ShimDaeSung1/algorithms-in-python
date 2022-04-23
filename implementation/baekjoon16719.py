import sys
input = sys.stdin.readline

str = list(input().rstrip())
#정답을 출력할 result배열
result = ['']*len(str)

# 사전순으로 먼저 오는 알파벳을 최대한 먼저 출력한다. 
# 대신 인덱스는 변하지 않는다. 마지막엔
# 같은 문자를 출력해야 하기 때문
# 사전순으로 먼저 오는 알파벳을 골랐으면
# 그 알파벳의 뒤로 그 다음으로 먼저오는 알파벳을
# 이어줘야 완성, 앞으로 이어주면 사전순서가 역순이됨
def func(arr, start):
    if not arr:
        return
    min_arr = min(arr)
    idx = arr.index(min_arr)
    result[start+idx] = min_arr
    print(''.join(result))
    func(arr[idx+1:], start+idx+1)
    func(arr[:idx], start)

    

func(str, 0)


