minguk = list(map(int, input().split()))
manse = list(map(int, input().split()))

if sum(minguk) > sum(manse) :
  print(sum(minguk))
else :
  print(sum(manse))
