t = int(input())

for tc in range(1, t + 1) :
    data = input()
    h = int(input())
    hyphen = list(map(int, input().split()))
    hyphen.sort()

    result = ""
    for i in range(len(data)) :
        if hyphen :
            while hyphen[0] == i :
                result += '-'
                hyphen.pop(0)
                if len(hyphen) == 0 :
                    break
        result += data[i]

    if hyphen :
        result += '-' * len(hyphen)

    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 하이픈 위치(hyphen) 리스트를 오름차순으로 정렬한다.
2. 입력받은 data 문자열의 문자를 하나씩 확인하며, 만약 hyphen 리스트에 요소가 존재하고 가장 첫 요소가 i와 다를 때까지 result에 '-' 문자를 넣어주고 hyphen 리스트에서 해당 요소를 제거한다.
3. 이후 만약 hyphen 리스트에 존재하는 요소가 없다면 break 한다.
4. result에 현재 문자(data[i])를 추가한다.
5. 반복문이 종료된 후 만약 hyphen 리스트에 요소가 아직 남아있다면 가장 마지막에 붙여야할 위치가 들어있으므로 result에 '-' 문자를 hyphen 리스트의 개수만큼 붙인다.
6. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
