data = input()

result = 0
for i in range(len(data)) :
    result += int(data[i])

print(result)

# 1. 자연수를 문자열 형태로 입력받아 각 자릿수를 정수형으로 변환하여 result 값에 누적한다. 이후 반복문 수행이 종료되면 result 값을 출력한다.
