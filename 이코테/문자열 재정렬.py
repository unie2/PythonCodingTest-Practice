s = input()
number = 0
al = []
for i in range(len(s)) :
  if(65 <= int(ord(s[i])) <= 90 ) :
    al.append(s[i])
  else :
    number += int(s[i])

al.sort()
al.append(str(number))

print(''.join(al))
