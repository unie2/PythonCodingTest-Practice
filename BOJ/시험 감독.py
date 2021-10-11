n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())

result = n

for i in range(n) :
  temp = people[i] - b

  if temp > 0 :
    temp1 = temp//c
    temp2 = temp%c

    if temp2 > 0 :
      temp2 = 1
    
    result += temp1 + temp2

print(result)
