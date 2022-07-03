while True :
    try :
        tc = int(input())
        target = input()
        data = input()

        result = data.count(target)

        print('#%d %d' % (tc, result))
    except :
        break
        
'''
1. 테스트 케이스의 개수가 주어지지 않았으므로 try ~ except 문을 포함시켜 코드를 구성한다.
2. 각 테스트 케이스마다 입력받은 data 문자열에서 찾고자 하는 target 문자열의 개수를 구해 result에 할당한다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
