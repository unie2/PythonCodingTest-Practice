n = int(input())

students = []

for _ in range(n) :
  students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students :
  print(student[0])
  
  
# 1. 반복문을 통해 students 리스트에 입력값을 추가한다.
# 2. lambda를 통해 students 리스트의 원소를 정렬하는데, 정렬 방식은 아래와 같다.
### (1) 두 번째 원소를 기준으로 내림차순 정렬
### (2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
### (3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
### (4) 네 번째 원소가 같은 경우, 첫 번재 원소를 기준으로 오름차순 정렬
# * sort( ) 함수의 key 속성에 값을 대입하여 내가 원하는 '조건'에 맞게 튜플을 정렬시킬 수 있다.
