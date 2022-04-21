'''조합(combinations) & 순열(permutations)'''


# 조합 구현 (중복 조합 X) : itertools 사용
from itertools import combinations

for i in combinations([1, 2, 3, 4], 3) :
    print(i, end=' ')
    # (1, 2, 3) (1, 2, 4) (1, 3, 4) (2, 3, 4)
print()

# 조합 구현 (중복 조합 O) : itertools 사용
from itertools import combinations_with_replacement

for i in combinations_with_replacement([1, 2, 3, 4], 2) :
    print(i, end=' ')
    # (1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4)
print()

#################################################################

# 제너레이터(generator)를 이용한 조합
# 조합 구현 (중복 조합 X) : itertools 미사용
def combinations(arr, r) :
    for i in range(len(arr)) :
        if r == 1 : # 종료 조건
            yield [arr[i]]
        else :
            for next in combinations(arr[i+1:], r - 1) :
                yield [arr[i]] + next

for i in combinations([1, 2, 3, 4], 3) :
    print(i, end=' ')
    # [1, 2, 3] [1, 2, 4] [1, 3, 4] [2, 3, 4]
print()

# 조합 구현 (중복 조합 O) : itertools 미사용
def combinations_2(arr, r) :
    for i in range(len(arr)) :
        if r == 1 : # 종료 조건
            yield [arr[i]]
        else :
            for next in combinations_2(arr[i:], r - 1) :
                yield [arr[i]] + next

for i in combinations_2([1, 2, 3, 4], 3) :
    print(i, end=' ')
print()


#################################################################


#################################################################

# 순열 구현 (중복 순열 X) : itertools 사용
from itertools import permutations

for i in permutations([1, 2, 3, 4], 2) :
    print(i, end=' ')
    # (1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)
print()


# 순열 구현 (중복 순열 O) : itertools 사용
from itertools import product

for i in product([1, 2, 3], 'ab') :
    print(i, end=' ')
    # (1, 'a') (1, 'b') (2, 'a') (2, 'b') (3, 'a') (3, 'b')
print()

for i in product(range(3), range(3), range(3)) :
    print(i, end=' ')
    # (0, 0, 0) (0, 0, 1) (0, 0, 2) (0, 1, 0) (0, 1, 1) (0, 1, 2) (0, 2, 0) (0, 2, 1) (0, 2, 2) (1, 0, 0) (1, 0, 1) (1, 0, 2) (1, 1, 0) (1, 1, 1) (1, 1, 2) (1, 2, 0) (1, 2, 1) (1, 2, 2) (2, 0, 0) (2, 0, 1) (2, 0, 2) (2, 1, 0) (2, 1, 1) (2, 1, 2) (2, 2, 0) (2, 2, 1) (2, 2, 2)
print()

for i in product([1, 2, 3], repeat=2) :
    print(i, end=' ')
    # (1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3)
print()


#################################################################

#################################################################

# 제너레이터(generator)를 이용한 순열
# 순열 구현 (중복 순열 X)
def permutations_1(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            for next in permutations_1(arr[:i] + arr[i+1:], r - 1) :
                yield [arr[i]] + next

for i in permutations_1([1, 2, 3, 4], 2) :
    print(i, end=' ')
    # [1, 2] [1, 3] [1, 4] [2, 1] [2, 3] [2, 4] [3, 1] [3, 2] [3, 4] [4, 1] [4, 2] [4, 3]
print()

for i in permutations_1('abcde', 2) :
    print(i, end=' ')
    # ['a', 'b'] ['a', 'c'] ['a', 'd'] ['a', 'e'] ['b', 'a'] ['b', 'c'] ['b', 'd'] ['b', 'e'] ['c', 'a'] ['c', 'b'] ['c', 'd'] ['c', 'e'] ['d', 'a'] ['d', 'b'] ['d', 'c'] ['d', 'e'] ['e', 'a'] ['e', 'b'] ['e', 'c'] ['e', 'd']
print()

# 순열 구현2 (중복 순열 X)
def permutations_2(arr, r, prefix="nothing") :
    for i in range(len(arr)) :
        if arr[i] == prefix :
            continue
        if r == 1 :
            yield [arr[i]]
        else :
            prefix = arr[i]
            for next in permutations_2(arr, r - 1, prefix) :
                yield [arr[i]] + next

for i in permutations_2(range(5), 2) :
    print(i, end=' ')
    # [0, 1] [0, 2] [0, 3] [0, 4] [1, 0] [1, 2] [1, 3] [1, 4] [2, 0] [2, 1] [2, 3] [2, 4] [3, 0] [3, 1] [3, 2] [3, 4] [4, 0] [4, 1] [4, 2] [4, 3]
print()



# 제너레이터(generator)를 이용한 순열
# 순열 구현 (중복 순열 O)
def permutations_3(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            for next in permutations_3(arr, r - 1) :
                yield [arr[i]] + next

for i in permutations_3([1, 2, 3], 3) :
    print(i, end=' ')
    # [1, 1, 1] [1, 1, 2] [1, 1, 3] [1, 2, 1] [1, 2, 2] [1, 2, 3] [1, 3, 1] [1, 3, 2] [1, 3, 3] [2, 1, 1] [2, 1, 2] [2, 1, 3] [2, 2, 1] [2, 2, 2] [2, 2, 3] [2, 3, 1] [2, 3, 2] [2, 3, 3] [3, 1, 1] [3, 1, 2] [3, 1, 3] [3, 2, 1] [3, 2, 2] [3, 2, 3] [3, 3, 1] [3, 3, 2] [3, 3, 3]
print()

