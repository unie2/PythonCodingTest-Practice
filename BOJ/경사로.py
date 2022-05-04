n, l = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0

def pos(now) :
    for j in range(1, n) :
        if abs(now[j] - now[j-1]) > 1 : # 차이가 1이 넘으면 False 반환
            return False
        if now[j] < now[j-1] : # 현재 < 이전 이면 경사로를 만들기 위해 오른쪽을 스캔(낮은 곳에 설치)
            for k in range(l) :
                if j+k >= n or used[j+k] or now[j] != now[j+k] : # 범위가 넘어가거나 이미 설치되어 있거나 높이가 다른 경우 False 반환
                    return False
                if now[j] == now[j+k] : # 높이가 같을 경우 방문 처리
                    used[j+k] = True
        elif now[j] > now[j-1] : # 현재 > 이전 이면 경사로를 만들기 위해 왼쪽을 스캔(낮은 곳에 설치)
            for k in range(l) :
                if j-k-1 < 0 or now[j-1] != now[j-k-1] or used[j-k-1] : # 범위가 넘어가거나 이미 설치되어 있거나 높이가 다른 경우 False 반환
                    return False
                if now[j-1] == now[j-k-1] : # 높이가 같을 경우 방문 처리
                    used[j-k-1] = True
    return True

# 가로 확인
for i in range(n) :
    used = [False for _ in range(n)] # 방문 처리
    if pos(data[i]) :
        result += 1

# 세로 확인
for i in range(n) :
    used = [False for _ in range(n)] # 방문 처리
    if pos([data[j][i] for j in range(n)]) :
        result += 1

print(result)

'''
1. n개의 줄의 지도를 입력받아 가로와 세로를 확인한다.
2. 각 반복문을 통해 방문 처리 리스트(used)를 정의하고 pos() 함수에 각 열에 있는 값들 혹은 각 행에 있는 값들을 리스트 형식으로 매개변수로 전달한다.
3. pos() 함수의 작업은 아래와 같다.
  - 값을 하나씩 확인하여 이전 값과의 차가 1이 넘으면 False를 반환한다.
  - 현재 값이 이전 값보다 작을 경우 경사로를 만들기 위해 l개 만큼 오른쪽을 스캔한다.
  - 스캔하는 값이 범위를 벗어나거나 이미 설치되어 있거나 현재 값과 높이가 다른 경우 False를 반환한다.
  - False가 반환되지 않았다면, 현재의 값과 스캔하는 값이 일치한지 확인하고, 일치하면 스캔하는 값의 인덱스를 used리스트 인덱스로 하여 방문처리를 진행한다.
  - 만약 현재 값이 이전 값보다 클 경우 경사로를 만들기 위해 l개 만큼 왼쪽을 스캔하며, 위 방식과 같은 방식으로 작업한다.
  - 위와 같은 과정의 반복작업이 모두 끝나면 True를 반환한다.
4. pos() 함수를 호출하여 True를 반환받았다면 result 값을 1 증가시키고, 이러한 작업이 모두 끝나면 최종적으로 result 값을 출력한다.

'''
