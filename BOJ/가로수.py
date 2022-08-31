import math

n = int(input())
data = []
diff_list = []
a = int(input()) # 첫번째 가로수 위치
data.append(a)
for _ in range(n - 1) :
    value = int(input())
    data.append(value)
    diff_list.append(value - a)
    a = value

def gcd(a, b) :
    if a % b == 0 :
        return b
    elif b == 0 :
        return a
    else :
        return math.gcd(b, a%b)

gcd_num = diff_list[0]
for i in range(1, len(diff_list)) :
    gcd_num = gcd(gcd_num, diff_list[i])

result = 0
for i in range(1, n) :
    diff = data[i] - data[i-1] - 1
    result += diff // gcd_num

print(result)

'''
1. n개의 가로수 위치를 data에 할당하고, 각 가로수마다 떨어져 있는 거리를 diff_list에 할당한다.
2. 각 가로수마다 떨어져 있는 거리의 최대 공약수를 구하여 gcd_num에 할당한다.
3. 모든 가로수가 gcd_num 간격이 되도록 새로 심어야 하는 가로수의 개수를 구하여 출력한다.

'''
