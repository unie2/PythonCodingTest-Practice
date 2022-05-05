t = int(input())
for i in range(1, t + 1) :
    n = int(input())
    result = ''
    for j in range(n) :
        al, count = input().split()
        result += al * int(count)

    num = 0
    print('#%d' % i)
    for j in range(len(result)) :
        print(result[j], end='')
        num += 1
        if num == 10 :
            num = 0
            print()
            
'''
1. 각 테스트 케이스마다 n을 입력받아 그 수만큼 반복문을 수행하는데, 문자와 숫자를 입력받아 각 al, count 에 할당한다.
2. 문자열 result 에 입력받은 문자(al)를 입력받은 숫자(count)만큼 추가한다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 result 문자열을 10개 단위씩 끊어 출력한다.

'''
