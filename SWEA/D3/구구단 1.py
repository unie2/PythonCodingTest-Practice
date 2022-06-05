t = int(input())

def check(n) :
    for i in range(1, 10) :
        if n % i == 0 and n // i < 10 :
            return True
    return False

for tc in range(1, t + 1) :
    n = int(input())
    flag = check(n)

    if flag :
        print('#%d %s' % (tc, 'Yes'))
    else :
        print('#%d %s' % (tc, 'No'))
        
'''
1. 각 테스트 케이스마다 입력받은 n을 check() 함수에 전달하여 1 이상 9 이하의 두 수의 곱으로 표현될 수 있는지 확인한다.

2. 반환받은 flag 값이 True일 경우 해당 테스트 케이스 번호와 함께 'Yes'를 출력하고, 그렇지 않다면 'No'를 출력한다.

3. check() 함수의 작업은 아래와 같다.
  - 1부터 9까지의 수를 각 n에 나누고, 만약 나머지 값이 0이거 몫이 9 이하일 경우 True를 반환한다.
  - 반복문이 끝날 때까지 True가 반환되지 않았다면 False를 반환한다.

'''
