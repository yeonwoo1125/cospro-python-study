def solution(usage):
	answer = 0
	if usage > 30:
		answer = 20 * 430 + 10 * 570 + (usage - 30) * 840
	elif usage > 20:
		answer = 20 * 430 + (usage - 20) * 570
	else:
		answer = usage * 430
	return answer

usage = 35
ret = solution(usage)

print("solution 함수의 반환 값은", ret, "입니다.")
