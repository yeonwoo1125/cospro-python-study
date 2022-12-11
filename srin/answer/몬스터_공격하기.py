def solution(attack, recovery, hp):
	count = 0
	while(True):
    # 공격 할때마다 count 1씩 증가
		count += 1
    # attack만큼 hp가 소모됨
		hp -= attack
    
    #만약, hp가 0이하면 while문을 빠져나옴
		if hp <= 0:
			break
      
    # 힐링마법은 항상 같은 수치로 hp를 증가시킴
		hp += recovery
	return count

attack = 30
recovery = 10
hp = 60
ret = solution(attack, recovery, hp)

print("solution 함수의 반환 값은", ret, "입니다.")
