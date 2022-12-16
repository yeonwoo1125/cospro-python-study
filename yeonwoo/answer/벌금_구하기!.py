def solution(speed, cars):
	answer = 0
	for x in cars:
		if x >= speed * 11 / 10 and x < speed * 12 / 10:
			answer += 3
		elif x >= speed * 12 / 10 and x < speed * 13 / 10:
			answer += 5
		elif x >= speed * 13 / 10:
			answer += 7
	return answer

if __name__ == '__main__':
  speed = 100
  cars = [110, 98, 125, 148, 120, 112, 89]
  ret = solution(speed, cars)

  print("solution 함수의 반환 값은", ret, "입니다.")
