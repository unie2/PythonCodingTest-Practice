def func(index) :
    global data

    for i in range(1, (index // 2) + 1) :
        if data[-i:] == data[-2*i:-i] :
            return -1

    if index == n :
        for i in range(n) :
            print(data[i], end='')
        return 0

    for i in range(1, 4) :
        data.append(i)
        if func(index + 1)  == 0:
            return 0
        data.pop()

n = int(input())
data = []
func(0)

'''
1. 좋은 수열을 판단하고 가장 작은 수를 도출해내는 func() 함수의 작업은 아래와 같다.
  - 1부터 index의 절반까지를 반복문의 범위로 하여 해당 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면 -1을 반환한다.
  - -1이 반환되지 않았다면, index값과 n을 확인하여 두 수가 같다면 n개의 길이의 수를 도출해냈으므로 값을 출력하고, 0을 반환한다..
  - 그렇지 않다면 값을 더 추가해야하므로, data 리스트에 값을 추가하고 func() 함수를 재귀호출하여 반환받은 값은 값이 0이라면 0을 반환한다.
  - func() 함수를 재귀호출하여 반환받은 값이 -1이라면 나쁜 수열이므로 data 리스트의 가장 마지막 요소를 제거한다.

'''
