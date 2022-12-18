def solution(score):
	answer = [ 1 for i in range(len(score))]
	for i in range(len(score)):
		for j in range(len(score)):
			if score[i] < score[j]:
				answer[i] += 1
	return answer

if __name__ == '__main__':
  score1 = [90, 87, 87, 23, 35, 28, 12, 46]
  ret1 = solution(score1)

  print("solution 함수의 반환 값은", ret1, "입니다.")

  score2 = [10, 20, 20, 30]
  ret2 = solution(score2)

  print("solution 함수의 반환 값은", ret2, "입니다.")
