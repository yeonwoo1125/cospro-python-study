def solution(number):
	count = 0
	for i in range(1, number + 1):
		current = i
		while current != 0:
			lastNum = current % 10
			if lastNum == 3 or lastNum == 6 or lastNum == 9:
				count += 1
			current = current // 10
	return count


if __name__ == '__main__':
  number = 40
  ret = solution(number)

  print("solution 함수의 반환 값은", ret, "입니다.")
