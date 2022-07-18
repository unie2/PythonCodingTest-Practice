from itertools import combinations

while True :
    try :
        data = list(map(int, input().split()))
        if data[0] == 0 and len(data) == 1 :
            break
        del data[0]

        result = []
        for combi in combinations(data, 6) :
            combi = sorted(combi)
            result.append(combi)

        result.sort()
        for value in result :
            print(' '.join(map(str, value)))

        print()
    except :
        break
        
'''
1. 입력은 여러 개의 테스트 케이스로 이루어져 있으므로 while 내부에 try ~ except 문을 삽입하여 코드를 작성한다.
2. data를 리스트 형태로 입력받고, 만약 입력받은 값이 1개이고 그 값이 0일 경우 break한다.
3. data리스트의 0번째 요소를 삭제한다.
4. combinations() 를 통해 6개의 값을 도출하는 경우를 구하고 오름차순으로 정렬한 값을 result 리스트에 할당한다.
5. combinations() 작업을 마치면 result 리스트를 오름차순으로 정렬하여 문제에서 요구하는 출력 형식에 맞추어 값을 출력한다.

'''
