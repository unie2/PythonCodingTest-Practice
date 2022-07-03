while True :
    try :
        tc = int(input())
        data = []
        result = 0
        diagonal = 0
        idx = 0
        # 가로
        for _ in range(100) :
            temp = list(map(int, input().split()))
            data.append(temp)
            result = max(result, sum(temp))
            diagonal += temp[idx]
            idx += 1
        # 세로
        data = list(zip(*data))
        for i in range(100) :
            result = max(result, sum(data[i]))

        result = max(result, diagonal)

        print('#%d %d' % (tc, result))

    except :
        break
        
'''
1.테스트 케이스의 개수가 주어지지 않았으므로 try ~ except 문을 포함시켜 코드를 구성한다.
2. 각 테스트 케이스마다 100x100 크기의 데이터를 한 줄씩 입력받아 data 리스트에 추가하고, 해당 데이터들의 합과 현재의 result 값을 비교하여 더 큰 값을 result에 할당한다.
3. 또한, 대각선의 합을 구하기 위해 idx 값을 이용하여 temp[idx] 값을 diagonal에 누적한 후 idx를 1 증가시킨다.
4. 이후 세로의 합을 구하기 위해 zip()을 사용하여 data 리스트 요소의 행과 열을 바꾼다.
5. 행과 열이 바뀌었으므로 특정 행에 존재하는 열 값들을 모두 합한 값을 구하고, result 값과 비교하여 더 큰 값을 result에 할당한다.
6. 현재의 result 값과 대각선의 합(diagonal)을 비교하여 더 큰 값을 result에 할당하고, 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
