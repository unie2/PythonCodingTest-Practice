a_attack, a_hp = map(int, input().split())
b_attack, b_hp = map(int, input().split())

while True :
  a_hp -= b_attack
  b_hp -= a_attack
  if a_hp <= 0 or b_hp <= 0 :
    break

if a_hp <= 0 and b_hp <= 0 :
  print("DRAW")
elif a_hp <= 0 :
  print("PLAYER B")
else :
  print("PLAYER A")
  
  
# 1. while문을 통해 A 생명력과 B 생명력 각각에 대하여 상대방의 공격력만큼 감소시킨 뒤  둘 중 하나라도 생명력이 0 이하가 되면 반복문을 종료한다.
# 2. 조건문을 통해 두 생명력 모두 0이하가 되어 모두 죽은 상태라면 "DRAW"를 출력한다.
# 3. 그렇지 않고 A의 생명력만 0이하라면 플레이어 B의 카드가 남아있기 때문에 "PLAYER B"를 출력한다.
# 4. 그렇지 않고 B의 생명력만 0이하라면 플레이어 A의 카드가 남아있기 때문에 "PLAYER A"를 출력한다.
