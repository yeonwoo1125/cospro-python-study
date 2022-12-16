def solution(people):
	answer = [0 for _ in range(4)]
	for height in people:
		if height < 95:
			answer[0] += 1
		elif height < 100:
			answer[1] += 1
		elif height < 105:
			answer[2] += 1
		else:
			answer[3] += 1
	return answer

if __name__ == '__main__':
  people = [97, 102, 93, 100, 107]
  ret = solution(people)

  print("solution 함수의 반환 값은", ret, "입니다.")
