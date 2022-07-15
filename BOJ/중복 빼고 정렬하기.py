n = int(input())
data = list(map(int, input().split()))

def merge_sort(data) :
    if len(data) <= 1 :
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    i, j = 0, 0
    temp = []

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            temp.append(left[i])
            i += 1
        else :
            temp.append(right[j])
            j += 1

    temp += left[i:]
    temp += right[j:]

    return temp

data = list(set(data))
data = merge_sort(data)


print(*data)

'''
1. 병합 정렬을 통해 시간 초과 판정을 받지 않고 문제를 해결할 수 있다.

2. 입력받은 n개의 값을 data 리스트에 저장하고 중복 제거를 수행한다.

3. merge_sort() 함수를 호출하여 정렬을 수행한 뒤, 정렬된 data 리스트의 값을 출력한다.

4. merge_sort() 함수의 작업은 아래와 같다.
  - 만약 전달받은 data 리스트 내 요소 개수가 1개 이하일 경우 정렬할 필요가 없으므로 해당 리스트를 그대로 반환한다.
  - 반환되지 않았다면 중간 위치 (data 리스트의 개수 / 2) 를 구하여 mid에 할당한다.
  - data 리스트의 중간 위치를 기준으로 하여 나누고, 왼쪽 배열을 left에, 오른쪽 배열을 right에 할당한다.
    이때 merge_sort() 함수를 재귀호출하여 정렬을 수행한 값을 할당하도록 한다.
  - i가 left 리스트 개수 이상이거나 j가 right 리스트 개수 이상일 때까지 while문 작업을 반복 수행한다.
  - while문 내부에서는 left[i] 값과 right[j] 값을 확인하여 더 작은 값을 temp 리스트에 저장하고 i 혹은 j 값을 1 증가시킨다.

  - while문이 끝난 후에는 left 리스트나 right 리스트 내에 남은 요소들을 temp 리스트에 추가한다.
  - 이후 정렬된 temp 리스트를 반환한다.

'''
