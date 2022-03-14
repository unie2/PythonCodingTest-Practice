a = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())
day = 0
for i in range(0, x - 1) :
  day += b[i]

result = (day + y) % 7

print(a[result])

'''
1. 결과를 출력할 요일이 담긴 리스트 a와 일 수가 담긴 리스트 b를 정의한다.
2. 반복문을 통해 1월부터 입력받은 x - 1월 까지의 일수를 day에 누적해나간다.
3. 반복문이 종료되면 day 값에 입력받은 y를 더한 뒤, 요일은 총 7개로 구성되어있으므로 7로 나눈 나머지 값을 구해 result에 할당한다.
4. 최종적으로 리스트 a의 result 번째의 값을 출력한다.

'''
