def solution(number):
	count = 0
	while number > 0:
		n = number % 10
		if n == 2 or n == 3 or n == 5 or n == 7:
			count += 1
		number //= 10
	return count

if __name__ == '__main__':
  number = 29022531
  ret = solution(number)

  print("solution 함수의 반환 값은", ret, "입니다.")
