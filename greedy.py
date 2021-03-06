
#   가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유
#   가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.


#   for문을 사용해 array 길이만큼 반복 해준다.
#   array(화폐) 0번 인덱스 부터 계산을 시작하고 coin 변수에 값을 저장한다. for coin in array:
#   count 변수에 n(잔돈)을 coin(화폐)으로 나누어 저장한다. (n//coin)  // 왼쪽 변수에 오른쪽 값을 나눈 후 정수 몫을 왼쪽 변수에 할당.
#   계산 후 남은 n(잔돈), 즉 나머지값을 n에 저장한다. (n %= coin) === (n = n % coin) 여기서의 n값은 당연히 1260, 260, 60, 10
#   반복문이 끝날 때까지 처음부터 시작한다.
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    #print(n)
    count += n // coin
    #print(coin)
    n %= coin # n = n%coin

print(count)






