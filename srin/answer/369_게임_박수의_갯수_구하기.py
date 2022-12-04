def solution(number):
	count = 0
	for i in range(1, number + 1):
		current = i
		while current != 0:
			if current%10==3 or current%10==6 or current%10==9:
				count += 1
			current = current // 10
	return count

number = 40
ret = solution(number)

print("solution 함수의 반환 값은", ret, "입니다.")
