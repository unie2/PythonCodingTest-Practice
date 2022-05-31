def solution(arr) :
    answer = [0, 0]
    len_value = len(arr)

    def func(x, y, len_v) :
        temp = arr[x][y]
        for i in range(x, x + len_v) :
            for j in range(y, y + len_v) :
                if arr[i][j] != temp :
                    temp_len_v = len_v // 2
                    func(x, y, temp_len_v)
                    func(x, y + temp_len_v, temp_len_v)
                    func(x + temp_len_v, y, temp_len_v)
                    func(x + temp_len_v, y + temp_len_v, temp_len_v)
                    return
        answer[temp] += 1

    func(0, 0, len_value)
    return answer
  
'''
1. len_value에 arr리스트의 크기를 할당하고, func() 함수를 호출하여 작업을 수행한 후 answer 리스트를 반환한다.

2. func() 함수의 작업은 아래와 같다.
  - 전달받은 좌표(x, y)를 temp에 담아 확인하고 있는 값(arr[i][j])이 temp와 다를 경우 4칸으로 나눠 func() 함수를 재귀 호출한다.
  - 이러한 방식으로 크기가 1까지 도달하면 1씩 더해주도록 한다.

'''
