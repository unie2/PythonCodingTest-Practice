data = []

people = 0
for i in range(10) :
  bye, hello = map(int, input().split())
  people = people - bye + hello
  data.append(people)

print(max(data))
