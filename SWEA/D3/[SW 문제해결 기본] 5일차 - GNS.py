t = int(input())

info = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, t + 1) :
    num, n = input().split()
    data = list(input().split())

    for i in range(int(n)) :
        data[i] = info.index(data[i])

    data.sort()
    for i in range(int(n)) :
        data[i] = info[data[i]]

    print('#%d' % tc)
    print(*data)
    
'''
1. "ZRO" ~ "NIN" 까지의 문자열을 info 리스트에 담는다.
2. 각 테스트 케이스마다 n개의 문자열을 입력받아 data 리스트에 저장한다.
3. data 리스트의 각 요소를 통해 info 리스트의 해당 인덱스를 찾아 data[i]에 갱신한다.
4. data 리스트를 오름차순으로 정렬한 후, 다시 data[i]를 인덱스로 하여 info 리스트에서 문자열을 가져와 data[i]에 할당한다.
5. 최종적으로 해당 테스트 케이스 번호와 함께 data 리스트의 요소를 출력한다.

'''
