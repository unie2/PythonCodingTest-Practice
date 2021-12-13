a, b = input().split()

min_value = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max_value = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min_value, max_value)


# 1. 문자열 a의 문자 중 '6'을 '5'로 변환하고, 문자열 b의 문자 중 '6'을 '5'로 변환한다.
# 2. 변환된 두 문자열을 각각 정수형으로 변환하여 더한 값을 min_value에 할당한다.
# 3. 문자열 a의 문자 중 '5'를 '6'으로 변환하고, 문자열 b의 문자 중 '5'를 '6'으로 변환한다.
# 4. 변환된 두 문자열을 각각 정수형으로 변환하여 더한 값을 max_value에 할당한다.
