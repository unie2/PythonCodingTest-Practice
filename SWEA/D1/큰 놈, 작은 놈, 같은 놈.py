t = int(input())

for i in range(1, t + 1) :
    a, b = map(int, input().split())
    if a == b :
        print('#%d %s' % (i, '='))
    elif a < b :
        print('#%d %s' % (i, '<'))
    else :
        print('#%d %s' % (i, '>'))
        
'''
1. 각 테스트 케이스마다 2개의 수를 입력받아 해당 테스트 케이스 번호와 함께 아래와 같이 출력한다.
  - a와 b의 값이 같을 경우 '='를 출력한다.
  - a의 값이 b의 값보다 작을 경우 '<'를 출력한다.
  - b의 값이 a의 값보다 작을 경우 '>'를 출력한다.

'''
