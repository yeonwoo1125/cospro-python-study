def solution(taekwondo, running, shooting):
	answer = 0
	if taekwondo >= 25:
		answer += 250
	else:
		answer += taekwondo * 8
	answer += 250 + (60 - running) * 5
	count = 0
	for s in shooting:
		answer += s
		if s == 10:
			count += 1
	if count >= 7:
		answer += 100
	return answer

if __name__ == '__main__':
  taekwondo = 27
  running = 63
  shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
  ret = solution(taekwondo, running, shooting)

  print("solution 함수의 반환 값은", ret, "입니다.") 
