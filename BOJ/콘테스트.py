w_data = []
k_data = []

for i in range(20) :
  if i < 10 :
    w_data.append(int(input()))
  else :
    k_data.append(int(input()))

w_data.sort(reverse=True)
k_data.sort(reverse=True)

print(sum(w_data[:3]), sum(k_data[:3]))


# 1. 반복문을 통해 앞 10개의 입력 점수를 W 대학(w_data) 리스트에 추가하고 뒤 10개의 입력 점수를 K 대학(k_data) 리스트에 추가한다.
# 2. 두 리스트를 내림차순으로 정렬한다.
# 3. 최종적으로 출력 시 내림차순으로 정렬된 각 리스트의 앞 3개의 점수를 합하여 출력한다.
