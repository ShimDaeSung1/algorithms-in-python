# 문제
# 춘향이는 편의점 카운터에서 일한다.

# 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.

# 예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

# 입력
# 첫째 줄에 거스름돈 액수 n(1 ≤ n ≤ 100,000)이 주어진다.

# 출력
# 거스름돈 동전의 최소 개수를 출력한다. 만약 거슬러 줄 수 없으면 -1을 출력한다.
import sys
input = sys.stdin.readline # 리턴 값이 문자열

money = int(input())
# money = int(input("거스름돈을 받을 액수를 입력하시오"))
count = 0

if money < 5:
    if money % 2 != 0:
        count = -1
    else:
        count += money//2
else: 
    count, n = divmod(money, 5) # money를 5로 나눈 몫과 나머지
    if n == 0:
        count = count
    else :
        if n % 2 == 0:
            count += n // 2
        else:
            count -= 1
            n += 5
            count += n // 2
print(count)

          








