# # 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어질 때
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
# 'X'혹은 '+'연산자를 넣어 결과적으로 만들어질 수 있는
# 가장 큰 수를 구하는 프로그램 작성하기
# 모든 연산은 왼쪽으로부터 순서대로 이루어진다.
# EX) 02984 --> ((((0+2)x9)x8)x4) = 576

# 입력 조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어진다. (1 <= S <= 20)
# 출력 조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수 출력

# 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하고, 두 수가 모두 2 이상인 경우에는 곱하면 된다.

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입한다.
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num

print(result)
