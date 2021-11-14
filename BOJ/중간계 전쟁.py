tc = int(input())

for i in range(1, tc + 1) :
  gan = list(map(int, input().split()))
  sau = list(map(int, input().split()))

  gan_score = gan[0] + gan[1]*2 + gan[2]*3 + gan[3]*3 + gan[4]*4 + gan[5]*10
  sau_score = sau[0] + sau[1]*2 + sau[2]*2 + sau[3]*2 + sau[4]*3 + sau[5]*5 + sau[6]*10

  if gan_score > sau_score :
    print(f"Battle {i}: Good triumphs over Evil")
  elif gan_score < sau_score :
    print(f"Battle {i}: Evil eradicates all trace of Good")
  else :
    print(f"Battle {i}: No victor on this battle field")
    
    
# 1. 간달프 군대에 참여한 종족의 수와 사우론 군대에 참여한 종족의 수를 입력받아 각각 리스트 형태로 구성한다.
# 2. gan_score에 입력받은 gan리스트의 각 인덱스 값과 문제에서 제시한 군대의 각 종족의 점수를 곱하여 누적한다.
# 3. sau_score에 입력받은 sau리스트의 각 인덱스 값과 문제에서 제시한 군대의 각 종족의 점수를 곱하여 누적한다.
# 4. 조건문을 통해 간달프 군대가 이긴다면 "Good triumphs over Evil"를, 사우론의 군대가 이긴다면 "Evil eradicates all trace of Good", 점수의 합이 같아 이기는 쪽이 없다면 "No victor on this battle field"를 출력한다.
