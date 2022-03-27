import sys
input = sys.stdin.readline

a = int(input())
data= list(map(int, input().split()))
increase = [1] * a
decrease = [1] * a

for i in range(a) :
	for j in range(i) :
		if data[j] < data[i] :
			increase[i] = max(increase[i], increase[j] + 1)

for i in range(a-1, -1, -1) :
	for j in range(a-1, i, -1) :
		if data[j] < data[i] :
			decrease[i] = max(decrease[i], decrease[j] + 1)

result = [0] * a
for i in range(a) :
	result[i] = increase[i] + decrease[i] - 1

print(max(result))

'''
1. 증가하는 수열의 길이와 감소하는 수열의 길이를 각각 구하기 위해 increase와 decrease를 a 크기 만큼 1로 초기화한다.
2. 첫번째 2중 for문을 통해 각 인덱스를 기준으로 증가하는 수열의 길이를 구한다.
3. 두번째 2중 for문을 통해 각 인덱스를 기준으로 감소하는 수열의 길이를 구한다. 여기서는 값을 거꾸로 확인한다.
4. 최종적으로 증가하는 수열의 특정 인덱스값과 감소하는 수열의 특정 인덱스값을 더하고, 특정 기준 값이 중복되므로 1을 빼주어 result[i]에 할당한다.
5. result 리스트 내 요소들 중 가장 큰 값을 출력한다.

'''
