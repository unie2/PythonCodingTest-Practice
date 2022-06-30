for tc in range(1, 11) :
    n = int(input())
    data = list(map(int, input().split()))
    o = int(input())
    order = list(input().split())

    type = ''
    pos = -1
    cnt = -1
    for i in range(len(order)) :
        if order[i] in ['I', 'D'] :
            type = order[i]
            pos = -1
            cnt = -1
        else :
            if type == 'I' : # 삽입
                if pos == -1 :
                    pos = int(order[i])
                    continue
                else :
                    if cnt == -1 :
                        cnt = int(order[i])
                        continue

                    data.insert(pos, order[i])
                    pos += 1
            elif type == 'D' : # 삭제
                if pos == -1 :
                    pos = int(order[i])
                    continue
                else :
                    if cnt == -1 :
                        cnt = int(order[i])
                        for j in range(cnt) :
                            del data[pos]

    print('#%d' % tc, end=' ')
    print(*data[:10])
    
'''
1. 각 테스트 케이스마다 원본 암호문(data)과 명령어(order)를 리스트 형태로 구성한다.

2. order 리스트의 요소를 순서대로 하나씩 확인하며, 만약 해당 값이 'I' 혹은 'D'일 경우 type을 해당 문자로 갱신하고, pos와 cnt를 -1로 설정한다.

3. 해당 값이 숫자라면 아래와 같은 작업을 수행한다.
  - 만약 type이 'I'이고 pos가 -1이라면, 현재 값이 삽입할 위치를 의미하므로 pos에 해당 값(정수형으로 변환)을 할당하고 continue한다.
  - 만약 type이 'I'이고 pos가 -1이 아니고 cnt가 -1이라면, 현재 값이 삽입할 값의 개수를 의미하므로 cnt에 해당 값(정수형으로 변환)을 할당하고 continue한다.
  - cnt가 -1인지 확인하는 부분까지 continue가 되지 않았다면, 현재의 값이 삽입할 값을 의미하므로 data리스트의 pos 위치에 해당 값을 삽입한 후 pos 값을 1 증가시킨다.
 
  - 만약 type이 'D'이고 pos가 -1이라면, 현재 값이 삭제할 위치를 의미하므로 pos에 해당 값(정수형으로 변환)을 할당하고 continue한다.
  - 만약 type이 'D'이고 pos가 -1이 아니고 cnt가 -1이라면, 현재 값이 삭제할 값의 개수를 의미하므로 cnt에 해당 값(정수형으로 변환)을 할당한다.
  - 할당된 cnt개 만큼 pos위치에 존재하는 값을 삭제한다.

4. 최종적으로 해당 테스트 케이스 번호와 함께 암호문의 처음 10개 항을 출력한다.

'''
