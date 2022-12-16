def solution(scores, cutline):
	answer = 0
	for score in scores:
		if score >= cutline:
			answer += 1
	return answer

if __name__ == '__main__':
  scores = [80, 90, 55, 60, 59]
  cutline = 60
  ret = solution(scores, cutline)

  print("solution 함수의 반환 값은", ret, "입니다.")
