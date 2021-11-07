n = int(input())

first_discount = n * (22/100)
first_result = int(n - first_discount)

second_n = n - (n * (80/100))
second_discount = second_n * (22/100)
second_result = int(n - second_discount)

print(first_result, second_result)


# 1. 전체 상금의 22%를 제세공과금으로 납부하는 경우
#   - first_discount에 입력받은 상금(n)에서 22%의 값을 할당한다.
#   - first_result에 상금(n)에서 22% 할인한 총 금액을 할당한다.

# 2. 상금의 80%를 필요 경비로 인정받고, 나머지 금액 중 22%만을 제세공과금으로 납부하는 경우
#   - second_n에 입력받은 상금(n)의 20%를 구하여 할당한다.
#   - second_discount에 상금 20%에서 22%의 값을 할당한다.
#   - second_result에 상금(n)에서 22% 할인한 총 금액을 할당한다.
# 최종적으로 first_result와 second_result를 출력한다.
