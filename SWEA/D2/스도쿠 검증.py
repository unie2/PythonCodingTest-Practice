t = int(input())
 
def check_1(data) :
    value = [0] * 10
    for i in range(9) :
        for j in range(9) :
            value[data[i][j]] += 1
            value[data[j][i]] += 1
        if value.count(2) != 9 :
            return False
        value = [0] * 10
    return True
 
def check_2(data) :
    value = [0] * 10
    for i in range(0, 9, 3) :
        for j in range(0, 9, 3) :
            for k in range(i, i+3) :
                for l in range(j, j+3) :
                    value[data[k][l]] += 1
            if value.count(1) != 9 :
                return False
            value = [0] * 10
    return True
     
 
for i in range(1, t + 1) :
    data = [list(map(int, input().split())) for _ in range(9)]
    if check_1(data) == False :
        print('#%d %d' % (i, 0))
    else :
        if check_2(data) == False :
            print('#%d %d' % (i, 0))
        else :
            print('#%d %d' % (i, 1))
            
'''
1. 각 테스트 케이스마다 스도쿠 상태를 입력받아 매개변수로 하여 check_1() 함수를 호출한다. check_1() 함수의 작업은 아래와 같다.
  - 각 1~9 숫자가 등장한 횟수를 담는 value 리스트를 정의한다.
  - 2중 for문을 통해 data[i][j]와 data[j][i]를 인덱스로 하여 value 리스트의 해당 요소의 값을 1 증가시킨다.
  - 내부 반복문이 끝날 때마다 value 리스트 값들을 확인하여 2가 9개 존재하지 않을 경우 False를 반환한다.
  - 그렇지 않을 경우 다음 상황을 확인하기 위해 value리스트를 다시 0이 담긴 값들을 구성하여 초기화한다.
  - 모든 반복 작업에 이상이 없다면 True를 반환한다.

2. check_1() 함수를 통해 반환받은 값이 False라면 겹치는 숫자가 있으므로 해당 테스트 케이스 번호와 함께 0을 출력한다.

3. check_1() 함수를 통해 반환받은 값이 True라면 check_2() 함수를 호출한다. check_2() 함수의 작업은 아래와 같다.
  - 각 1~9 숫자가 등장한 횟수를 담는 value 리스트를 정의한다.
  - 4중 for문을 통해 9개의 값씩 확인할 수 있도록 하며, data[k][l]을 인덱스로 하여 value 리스트의 해당 요소의 값을 1 증가시킨다.
  - 9개의 값에 대한 확인을 마칠 때마다 value 리스트 값들을 확인하여 1이 9개 존재하지 않을 경우 False를 반환한다.
  - 그렇지 않을 경우 다음 상황을 확인하기 위해 value리스트를 다시 0이 담긴 값들을 구성하여 초기화한다.
  - 모든 반복 작업에 이상이 없다면 True를 반환한다.

4. check_2() 함수를 통해 반환받은 값이 False라면 겹치는 숫자가 있으므로 해당 테스트 케이스 번호와 함께 0을 출력한다.

5. check_2() 함수를 통해 반환받은 값이 True라면 올바른 스도쿠 상태이므로 해당 테스트 케이스 번호와 함께 1을 출력한다.

'''
