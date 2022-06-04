from bisect import bisect_right

n = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(list(set(data)))

def search(data, right_value) :
    right_index = bisect_right(data, right_value)
    return right_index - 1

for target in data :
    print(search(sorted_data, target), end=' ')
    
'''
1. 입력받은 data 리스트의 요소의 중복을 제거하고 오름차순으로 정렬하여 sorted_data 리스트에 할당한다.
2. data 리스트의 요소(target)를 하나씩 가져와 search() 함수에 전달하여 반환받은 값을 출력한다.
3. search() 함수에서는 bisect_right() 을 통해 리스트에 가장 우측에 존재하는 right_value 값을 갖는 인덱스를 구하고, 1을 감소시켜 반환한다.

'''
