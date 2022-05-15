def solution(progresses, speeds) :
    answer = []
    index = 0
    while True :
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]

        cnt = 0
        for i in range(index, len(progresses)) :
            if progresses[i] >= 100 :
                cnt += 1
            else :
                break
        if cnt > 0 :
            answer.append(cnt)
            index += cnt


        if sum(answer) == len(progresses) :
            return answer
          
'''
1. whlie문을 수행하여 아래와 같이 작업을 반복 수행한다.
  - progresses의 각 요소에 해당 인덱스에 존재하는 speeds 값을 더한다.
  - progreeses의 index번째 요소를 확인하여 해당 수가 100 이상일 경우 cnt를 1 증가시키고, 100 미만일 경우 break한다.
  - 만약 cnt 값이 0보다 클 경우 배포할 작업이 있으므로 answer리스트에 cnt를 추가하고 index를 다음에 확인할 인덱스 값으로 갱신한다.

2. 위 작업을 반복 수행하다가 answer에 담겨있는 작업의 개수의 총 합이 progresses의 길이와 같을 경우 모든 작업에 대한 배포가 이루어졌으므로 answer 리스트를 반환한다.

'''
