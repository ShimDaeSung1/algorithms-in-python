import sys
input = sys.stdin.readline

#도시의 개수 입력
n = int(input())

#인접한 두 도시를 연결하는 도로의 길이가 제일 왼쪽 도로부터 N-1개의 자연수로 주어짐
len_list = list(map(int, input().split()))

#각 도시당 주유소 가격
oil_list = list(map(int, input().split()))

minVal = oil_list[0]
price = 0

for i in range(n-1):
    if minVal > oil_list[i]:
        minVal = oil_list[i]
    price += (minVal * len_list[i])

print(price)







