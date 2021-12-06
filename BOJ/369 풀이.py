n = int(input())

count = 0
for i in range(3, n+1) :
  count += str(i).count('3')
  count += str(i).count('6')
  count += str(i).count('9')

print(count)


# 1. 369게임 중 박수를 쳐야하는 첫 숫자는 3이므로 0이나 1부터 시작할 필요없이 반복문의 범위의 첫 수를 3으로 설정한다.
# 2. i를 문자열 형식으로 변환하여 3 혹은 6 혹은 9의 개수를 구해 count 값에 누적한다.
# 3. 최종적으로 count 값을 출력한다. (부분 성공)
