def solution(a, b):
	answer = 0
	for i in range(1, b + 1):
		if (b * i) % a == 0:
			answer = b * i
			break
	return answer

if __name__ == '__main__':
  a = 4
  b = 6
  ret = solution(a, b)

  print("solution 함수의 반환 값은", ret, "입니다.")
