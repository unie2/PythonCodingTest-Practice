from collections import deque

def solution(cacheSize, cities) :
    answer = 0
    data = deque()

    if cacheSize == 0 :
        return len(cities) * 5

    for city in cities :
        city = city.lower()
        if city in data :
            answer += 1
            data.remove(city)
        else :
            answer += 5
            if len(data) >= cacheSize :
                data.popleft()
        data.append(city)

    return answer
  
'''
1. 만약 cacheSize가 0이라면 모든 도시가 cacheSize보다 크므로 len(cities) * 5 를 반환한다.
2. cities의 city를 하나씩 확인하는데, 대소문자를 구분하지 않으므로 모두 소문자로 변환한다.
3. 만약 city가 data에 존재한다면 answer를 1 증가시키고 data에서 city를 제거한다.
4. 그렇지 않다면 answer를 5 증가시킨다. 이후 len(data)가 cacheSize보다 크거나 같다면 data의 가장 첫 요소를 제거한다.
5. answer 증가 및 data 요소 제거 작업 후에는 data에 city를 추가한다.
6. 모든 반복 작업을 마치면 최종적으로 answer 값을 반환한다.

'''
