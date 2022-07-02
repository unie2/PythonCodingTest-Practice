while True :
    try :
        tc = int(input())
        data = list(map(int, input().split()))
        cnt = 1
        while True :
            value = data.pop(0)
            value -= cnt
            if value <= 0 :
                data.append(0)
                break
            data.append(value)
            if cnt >= 5 :
                cnt = 0
            cnt += 1

        print(f'#{tc}', *data)
    except :
        break
        
'''
1. 정해진 테스트 케이스 갯수가 없으므로 while문 내부에 try ~ except 를 작성한다.

2. 각 테스트 케이스마다 아래와 같은 작업을 반복한다.
  - 입력받은 data 리스트의 가장 첫번째 요소를 꺼내 value에 할당한다.
  - value에서 cnt 값을 뺀다.
  - 만약 value 값이 0 이하일 경우 data 리스트에 0을 추가하고 break하여 해당 테스트 케이스 번호와 함께 data 리스트 요소를 출력한다.
  - break되지 않았다면, data 리스트에 value 값을 추가하고, cnt가 5 이상일 경우 cnt를 0으로 갱신한다.
  - 이후 cnt 값을 1 증가시킨다.

'''
