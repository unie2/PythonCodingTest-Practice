def solution(s) :
    answer = [] # 이진 변환 횟수, 제거된 0의 개수
    count_bin = 0
    count_zero = 0
    while s != '1' :
        # 1번 수행 : 모든 0을 제거
        count_zero += s.count('0')
        s = s.replace('0', '')
        # 2번 수행
        len_value = len(s)
        # 진법 변환
        s = bin(len_value)[2:]
        count_bin += 1


    answer.append(count_bin)
    answer.append(count_zero)
    return answer
  
'''
1. 이진 변환 횟수 count_bin과 제거된 모든 0의 개수를 의미하는 count_zero를 0으로 초기화한다.

2. s가 '1'이 될 때까지 while문을 통해 반복 수행하며 작업은 아래와 같다.
  - (1번 수행) s에 존재하는 '0'의 개수를 count_zero에 누적하고, '0'을 공백으로 치환한다.
  - (2번 수행) s의 길이를 len_value에 할당하고 이진 변환을 수행하여 앞에 존재하는 '0b' 이후의 값들을 s에 갱신한 후 count_bin을 1 증가시킨다.

3. while문이 종료되면 최종적으로 answer리스트에 count_bin과 count_zero를 추가하고 반환한다.

'''
