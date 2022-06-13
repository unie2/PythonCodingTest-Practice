date = [_ for _ in range(12)] # 월 정의
# 일 정의
for i in range(1, 13) :
    # 29일까지 있는 경우 : 2월
    if i == 2 :
        date[i-1] = [0 for _ in range(29)]
    # 30일까지 있는 경우 : 4, 6, 9, 11
    elif i in [4, 6, 9, 11] :
        date[i-1] = [0 for _ in range(30)]
    # 31일까지 있는 경우 : 1, 3, 5, 7, 8, 10, 12
    else :
        date[i-1] = [0 for _ in range(31)]

# 요일 정의
day = 4 # 현재 (1/1) 금요일
for i in range(12) :
    for j in range(len(date[i])) :
        date[i][j] = day % 7
        day += 1

t = int(input())
for tc in range(1, t + 1) :
    m, d = map(int, input().split())
    print('#%d %d' % (tc, date[m-1][d-1]))
    
'''
1. 12개의 요소를 담은 date 리스트를 정의한 후 2016년 1월부터 12월까지의 각 일 수의 개수를 date 리스트의 해당 월에 할당한다.
2. 이후 요일을 정의하는데, 1월 1일은 금요일이므로 day를 4로 초기화해주고 하루가 지날 때마다 day%7 값을 삽입한 후 day를 1 증가시킨다.
3. 각 테스트 케이스마다 m과 d를 입력받은 후 해당 테스트 케이스 번호와 함께 date[m-1][d-1]을 출력한다.

'''
