def solution(lottos, win_nums) :
    info = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = []
    cnt = 0

    for value in lottos :
        if value in win_nums :
            cnt += 1

    answer.append(info[cnt + lottos.count(0)]) # 최고 개수
    answer.append(info[cnt])

    return answer
  
  
'''
1. 각 당첨 내용에 대한 순위를 info 딕셔너리에 정의한다.
2. lottos의 값을 하나씩 확인하는데, 만약 해당 숫자가 win_nums 리스트에 존재한다면 cnt를 1 증가시킨다.
3. cnt와 lottos에 존재하는 0의 개수를 더한 값에 대응하는 info 딕셔너리 값을 answer 리스트에 추가한다. (최고 순위 번호)
4. cnt에 대응하는 info 딕셔너리 값을 answer 리스트에 추가한다. (최저 순위 번호)

'''
