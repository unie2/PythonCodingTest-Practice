def in_order(value) :
    if not data[value] :
        return int(oper[value])
    left = in_order(data[value][0])
    right = in_order(data[value][1])

    if oper[value] == '-' :
        return left - right
    elif oper[value] == '+' :
        return left + right
    elif oper[value] == '*' :
        return left * right
    else :
        return left / right

for tc in range(1, 11) :
    n = int(input())
    data = {i: [] for i in range(1, n + 1)}
    oper = {i: '' for i in range(1, n + 1)}
    for _ in range(n) :
        temp = input().split()
        oper[int(temp[0])] = temp[1]
        if len(temp) == 3 :
            data[int(temp[0])] += [int(temp[2])] # 왼쪽 자식
        elif len(temp) == 4 :
            data[int(temp[0])] += [int(temp[2])] # 왼쪽 자식
            data[int(temp[0])] += [int(temp[3])] # 오른쪽 자식

    result = int(in_order(1))
    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n개의 정점 정보를 입력받아 oper[int(temp[0])]에 temp[1]을 할당한다.

2. 만약 temp의 길이가 3일 경우 왼쪽 자식의 정보를 data[int(temp[0])]에 추가하고, 길이가 4일 경우 왼쪽 자식과 오른쪽 자식 정보를 추가한다.

3. in_order() 함수에서 반환받은 값을 정수형으로 변환하여 result에 담고, 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

4. in_order() 함수의 작업은 아래와 같다.
  - 전달받은 value를 인덱스로 한 data 값이 존재하지 않을 경우 oper[value]를 정수형으로 변환하여 반환한다.
  - in_order() 함수를 재귀호출하여 왼쪽 자식 노드와 오른쪽 자식 노드를 구한다.
  - 만약 oper[value]가 '-'일 경우 left - right 값을 반환한다.
  - 만약 oper[value]가 '+'일 경우 left + right 값을 반환한다.
  - 만약 oper[value]가 '*' 일 경우 left * right 값을 반환한다.
  - 만약 oper[value]가 '/' 일 경우 left / right 값을 반환한다.

'''
