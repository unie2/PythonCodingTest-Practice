for tc in range(1, 11) :
    n = int(input())
    data = list(input())

    index = 0
    while index < len(data) - 2 :
        if data[index].isdigit() :
            if data[index+1] == '*' :
                data[index] = str(int(data[index]) * int(data[index+2]))
                data.pop(index+1)
                data.pop(index+1)
                continue
        index += 1

    result = 0
    for value in data :
        if value.isdigit() :
            result += int(value)

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 계산식을 문자형 형태로 하여 data 리스트에 저장한다.

2. index를 0으로 초기화한 뒤 index값이 data 리스트의 크기의 - 2 이상이 될 때까지 아래 작업을 반복한다.
  - 만약 data[index] 값이 숫자이고, 다음 값이 '*' 일 경우 data[index]와 data[index+2] 값을 정수형으로 변환하여 곱하고
    문자 형태로 data[index]에 재할당한다.
  - data 리스트에서 index+1번째 요소를 두 번 빼낸다. (한 번 뺀 후 인덱스가 한 칸씩 당겨지기 때문에)
  - 반복문의 하나의 작업이 끝날 때 index 값을 1 증가시킨다.

3. result 값을 0으로 초기화시켜준 뒤 data 리스트의 요소를 하나씩 확인하고, 그 값이 숫자일 경우 정수형으로 변환하여 result에 누적한다.

4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
