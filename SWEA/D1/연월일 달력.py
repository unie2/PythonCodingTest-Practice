t = int(input())
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, t + 1) :
    data = input()
    result = [data[:4]]

    if int(data[4:6]) in month :
        result.append(data[4:6])
    else :
        print('#%d %d' % (i, -1))
        continue

    if 1 <= int(data[6:]) <= day[int(data[4:6])-1] :
        result.append(data[6:])
    else :
        print('#%d %d' % (i, -1))
        continue

    print('#%d %s' % (i, "/".join(result)))
    
'''
1. 1월부터 12월까지를 담은 month 리스트와 각 달에 해당하는 날짜까지의 정보를 담은 day 리스트를 정의한다.
2. 입력받은 값의 0번째부터 3번째까지는 연도에 해당하고, 이를 result에 리스트 형태로 담는다.
3. 입력받은 달이 month 리스트에 있다면 result 리스트에 추가하고, 없다면 -1을 출력하고 continue 한다.
4. 입력받은 일이 1 이상이고 해당 달에 해당하는 최대 날짜 이하일 경우 result 리스트에 추가하고, 범위 밖이라면 -1을 출력하고 continue 한다.
5. 최종적으로 continue 작업을 받지 않았을 경우 테스트 케이스 번호와 함께 result 값을 출력한다. 출력 시에는 join() 을 통해 "/"로 구분될 수 있도록 출력한다.

'''
