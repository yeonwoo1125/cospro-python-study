def solution(weight, boxes):
	answer = 0
	for x in boxes:
		if not(x >= weight * 9 / 10 and x <= weight * 11 / 10):
			answer += 1
	return answer

if __name__ == '__main__':
  weight = 600
  boxes = [653, 670, 533, 540, 660]
  ret = solution(weight, boxes)

  print("solution 함수의 반환 값은", ret, "입니다.")
