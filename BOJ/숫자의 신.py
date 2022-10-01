# https://www.acmicpc.net/problem/1422

from functools import cmp_to_key

k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
max_value = max(data)

for _ in range(k, n) : # n - k 만큼 가장 큰 수를 추가
    data.append(max_value)

data.sort(key=cmp_to_key(lambda x, y: int(str(y)+str(x)) - int(str(x)+str(y))))
print(*data, sep='')

'''
1. cmp_to_key()와 lambda 를 통해 주어진 값들의 정렬을 수행하여 문제를 해결할 수 있다.
 
2. k개의 수를 입력받아 data 리스트에 할당하고, 그 중 가장 큰 값을 max_value에 할당한다.
 
3. n-k 개만큼 max_value 값을 data 리스트에 추가한다.
 
4. 각 수를 문자로 변환하여 두 문자를 이어붙였을 때 더 큰 값을 구성하여 정렬을 수행한 뒤 data 리스트의 모든 수를 이어 붙여 출력한다.

'''

### 추가 ###
# cmp_to_key()에서 cmp란 compare 함수를 의미한다.

# compare 구조
def compare(x, y) :
    if x+y > y+x :
        return -1
    elif x+y == y+x :
        return 0
    else :
        return 1
        
# 활용
from functools import cmp_to_key

def compare(x, y) :
    if x+y > y+x :
        return -1
    elif x+y == y+x :
        return 0
    else :
        return 1

data = ['34', '37', '9', '31', '3']
print(sorted(data, key=cmp_to_key(compare)))

# [결과] ['9', '37', '34', '3', '31']
# 즉, '9'와 '37'의 경우 '937' > '379' 이므로 9가 먼저 온다.

'''
(1) return 음수 : 먼저 들어온 요소가 앞으로 정렬된다.
(2) return 0 : 바뀌지 않는다.
(3) return 양수 : 나중에 들어온 요소가 앞으로 정렬된다. (먼저 들어온 요소보다 앞에 배치)
'''

# 이와 같이 cmp_to_key를 활용해 조건에 따라 정렬을 수행할 수 있다.

### ###

# [참고] 
'''
[참고]
https://blog.pjookim.me/entry/Python-BOJ-1422-%EC%88%AB%EC%9E%90%EC%9D%98-%EC%8B%A0
https://velog.io/@heyday_7/python-%EC%A1%B0%EA%B1%B4-%EC%A0%95%EB%A0%AC-%ED%95%98%EA%B8%B0-cmptokey
'''
