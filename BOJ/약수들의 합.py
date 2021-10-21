while True :
  n = int(input())
  if n == -1 :
    break
  number = 2
  data = [1]

  for i in range(2, n) :
    if n % i == 0 :
      data.append(i)

  result = str(n) + " = 1" 
  if n == sum(data) :
    for j in range(1, len(data)) :
      result += " + " + str(data[j])

    print(result)
  else :
    print(str(n) + " is NOT perfect.")
