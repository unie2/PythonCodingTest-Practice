for tc in range(1, 11) :
    k = int(input())
    data = []
    result = 0

    # 가로
    for _ in range(8) :
        temp = input()
        data.append(temp)
        for i in range(8 - k + 1) :
            if temp[i:i+k] == temp[i:i+k][::-1] :
                result += 1
    data = list(zip(*data))
    # 세로
    for i in range(8) :
        for j in range(8 - k + 1) :
            if data[i][j:j+k] == data[i][j:j+k][::-1] :
                result += 1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 8개의 문자로 이루어진 문자열을 한 줄씩 입력받는데, 한 줄에 대하여 k개의 문자열이 회문이라면 result 값을 1 증가시킨다.
2. 세로로 회문을 검사하기 위해 zip()을 통해 data 리스트 요소의 행과 열을 바꾼다.
3. 이후 가로로 회문을 검사하는 방식과 비슷하게 코드를 구성하여 회문이 존재하면 result 값을 1 증가시킨다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
