def solution(dartResult):
    answer = []
    index = 0
    score_idx = -1

    while index < len(dartResult) :
        if dartResult[index].isdigit() :
            end_index = index
            while dartResult[end_index].isdigit() :
                end_index += 1
            if dartResult[end_index] == 'S' :
                answer.append(int(dartResult[index:end_index]))
            elif dartResult[end_index] == 'D' :
                answer.append(int(dartResult[index:end_index]) ** 2)
            elif dartResult[end_index] == 'T' :
                answer.append(int(dartResult[index:end_index]) ** 3)
            score_idx += 1
            index = end_index + 1
        else :
            if dartResult[index] == '*' :
                if score_idx == 0 :
                    answer[score_idx] *= 2
                else :
                    answer[score_idx - 1] *= 2
                    answer[score_idx] *= 2
            elif dartResult[index] == '#' :
                answer[score_idx] *= -1
            index += 1

    return sum(answer)
  
'''
1. dartResult의 요소를 확인하기 위한 인덱스(index)와 '*'가 등장했을 때 첫 번째 스타상의 점수만 적용될지를 판별하기 위한 score_idx를 정의한다.

2. index가 dartResult 길이보다 크거나 같을 때까지 while문을 통해 반복 수행하며 작업은 아래와 같다.
  - 현재 확인하고 있는 문자가 숫자일 경우 그 이후로 문자가 나올 인덱스를 구하고, 이후에 나온 문자가 'S'일 경우 이전까지 나온 숫자를 정수형으로 변환하여 answer에 추가한다.
  - 이후에 나온 문자가 'D'일 경우 이전까지 나온 숫자를 정수형으로 변환하고 2제곱 하여 answer에 추가한다.
  - 이후에 나온 문자가 'T'일 경우 이전까지 나온 숫자를 정수형으로 변환하고 3제곱 하여 answer에 추가한다.
  - score_idx 를 1 증가시키고 index는 end_index에 1을 더한 값으로 갱신한다.

  - 현재 확인하고 있는 문자가 숫자가 아니고 '*'일 경우 score_idx 값을 확인하여 그 값이 0일 경우 answer[score_idx] 값을 2배 하여 갱신한다.
  - 만약 score_idx 값이 0이 아닐 경우 이전의 값과 현재의 값에 각각 2배 하여 갱신한다.
  - 현재 확인하고 있는 문자가 '#'일 경우 answer[score_idx]를 음수로 변환하여 갱신한다.

  - 하나의 작업을 끝낼 때마다 index를 1 증가시켜 다음 문자를 확인할 수 있도록 한다.
  
3. 최종적으로 정수형으로 구성된 answer 리스트의 요소들의 합을 구해 반환한다.

'''
