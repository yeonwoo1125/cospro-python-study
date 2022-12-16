def solution(money, chairs, desks):
	answer = 0
	for chair in chairs:
		for desk in desks:
			price = chair + desk
			if answer < price and price <= money:
				answer = price
	return answer

if __name__ == '__main__':  
  money1 = 7
  chairs1 = [2, 5]
  desks1 = [4, 3, 5]
  ret1 = solution(money1, chairs1, desks1)

  print("solution 함수의 반환 값은", ret1, "입니다.")

  money2 = 7
  chairs2 = [3]
  desks2 = [5]
  ret2 = solution(money2, chairs2, desks2)

  print("solution 함수의 반환 값은", ret2, "입니다.")
