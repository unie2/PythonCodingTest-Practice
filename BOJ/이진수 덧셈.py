a, b = map(str, input().split())

a = int(a, 2)
b = int(b, 2)

sum_value = a + b

print(bin(sum_value)[2:])


# 입력받은 두 개의 이진수의 덧셈 결과를 출력한다. 이진수의 경우 앞에 0b가 붙기 때문에 2번째 자리부터 출력한다.
