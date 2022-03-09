
#   입력받은 문자열중 첫번째 인덱스를 int형으로 바꾸고 result에 할당한다.
#   반복문을 사용한다. range는 인덱스 두번째(1)부터 시작할 수 있게하고, 반복 횟수는 입력받은 값(len(data))만큼
#   0, 1일 때는 * 보다 + 하는 것이 더 큰 수를 만들 수 있으므로 if문을 사용한다.
#   0, 1일 아닐 때는 * 해준다.
#   값을 result에 더해주거나 곱해준 후 결과값을 출력

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= i or result <= 1:
        result += num
    else:
        result *= num

print(result)
