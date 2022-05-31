import math
from collections import defaultdict

def solution(fees, records):
    answer = []

    dict = {}
    total = defaultdict(int)
    # 주차한 시간
    for record in records :
        time, number, state = record.split() # 시간, 차량 번호, 상태(In or Out)
        hour, minutes = time.split(":")
        time = int(hour) * 60 + int(minutes)
        if number in dict : # 이미 입차되어 있다면
            total[number] += time - dict[number]
            del dict[number]
        else : # 입차할 경우
            dict[number] = time

    # 출차를 안 한 경우
    max_time = (23 * 60) + 59
    for num, t in dict.items():
        total[num] += max_time - t

    # 요금 계산
    basic_minutes, basic_fee, split_minutes, split_fee = fees
    for num, t in total.items() :
        cost = basic_fee
        if t > basic_minutes : # 추가 요금 발생
            cost += math.ceil((t - basic_minutes) / split_minutes) * split_fee # 올림 처리
        answer.append((num, cost))

    # 차량 번호 오름차순
    answer.sort()
    return [value[1] for value in answer]
  
'''
1. 특정 차량 번호에 대한 주차 시간을 담을 임시 dict 딕셔너리와 총 주차 시간을 담을 total 딕셔너리를 정의한다.

[주차한 시간 구하기]
2. records에서 시간, 차량 번호, 상태를 가져오고 시간을 분 단위로 변환하여 time을 갱신한다.
3. 만약 dict 딕셔너리에 해당 차량번호(number)가 있을 경우 이미 입차되어 있으므로
   total[number]에 time - dict[number] 값을 누적하고 dict 딕셔너리에서 해당 차량번호에 대한 정보를 삭제한다.
4. dict 딕셔너리에 해당 차량번호가 존재하지 않고 입차할 경우 dict 딕셔너리에서 해당 차량번호에 대한 시간을 삽입한다.

[출차를 하지 않은 경우 처리]
5. 이후 출차를 하지 않은 경우를 처리하는데,  max_time에 23:59를 분 단위로 하여 담는다.
6. dict 딕셔너리에서 차량 번호와 시간을 가져오고 total[num]에 max_time - t 값을 누적한다.

[차량 번호에 대한 요금을 계산]
7. 이후 요금을 계산하는데, 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)을 fees에서 가져와 각 변수에 할당한다.
8. total 딕셔너리에서 차량 번호와 시간을 가져와 cost에 기본 요금을 먼저 할당하고 만약 기본 시간보다 더 오래 주차를 했다면 추가 요금을 cost에 누적한다.
9. 정의된 cost 값을 answer 리스트에 (차량 번호, 지불할 요금) 형태로 담고,
   모든 차량에 대한 요금이 answer 리스트에 다 담기면 차량 번호를 오름차순으로 하여 정렬하고 요금만 추출해 반환한다.

'''
