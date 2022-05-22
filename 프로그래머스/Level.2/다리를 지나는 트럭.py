def solution(bridge_length, weight, truck_weights) :
    answer = 0
    bridge = [0] * bridge_length
    now_weight = 0

    while truck_weights :
        # 트럭 빠짐
        now_weight -= bridge.pop(0)

        if truck_weights[0] + now_weight <= weight :
            # 새 트럭 추가
            bridge.append(truck_weights.pop(0))
            now_weight += bridge[-1]
        else :
            bridge.append(0)
        answer += 1

    return answer + bridge_length
  
'''
1. 다리 길이만큼의 bridge 리스트를 정의하고, 현재 다리 위에 존재하는 트럭의 무게 합을 담을 수 있는 now_weight를 정의한다.

2. truck_weights 리스트가 빌 때까지 아래와 같은 작업을 반복 수행한다.
  - bridge 리스트의 제일 앞 요소를 제거하면서 now_weight에서 값을 뺀다.
  - 만약 다리 위로 갈 새 트럭의 무게와 현재 무게를 더한 값이 weight 이하일 경우 bridge 리스트에 트럭을 추가한 후 now_weight에 무게를 더한다.
  - 다리에 들어갈 수 없을 경우 0을 추가한다.
  - bridge에 값을 추가했으면 answer을 1 증가시킨다.

3. 반복문이 끝나면 최종적으로 answer을 반환하는데, 마지막 트럭이 다리를 끝까지 건너가야하는 시간이 포함되어야하므로 bridge_length를 더하여 반환한다.

'''
