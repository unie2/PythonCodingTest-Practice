info = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t = int(input())
for i in range(1, t + 1) :
    month, day, next_month, next_day = map(int, input().split())
    result = 0
    if month == next_month :
        result += next_day - day + 1
    else :
        result += next_day
        for j in range(next_month-1, month, -1) :
            result += info[j]
        result += info[month] - day + 1

    print('#%d %d' % (i, result))
    
'''
1. 각 테스트 케이스마다 첫 번째 날짜와 두 번째 날짜를 입력받는다.
2. 첫 번째 월(month)과 두 번째 월(next_month)이 같을 경우 (next_day - day + 1) 값을 구하여 result에 누적한다. (1일도 포함이므로)
3. 월이 다를 경우 우선적으로 두 번째 일을 result에 누적하고, 반복문을 통해 두 월 사이에 존재하는 달의 일 수들을 result에 누적한다.
   이후 첫 번째 월(month) 의 일 수(info)에서 day를 빼고 1을 더한 값을 result에 누적한다.
4. 최종적으로 해당 테스크 케이스 번호와 함께 result 값을 출력한다.

'''
