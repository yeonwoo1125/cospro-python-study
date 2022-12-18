def solution(korean, english):
	answer = 0
	math = 210 - (korean + english)
	if math > 100:
		answer = -1
	else:
		answer = math
	return answer

korean = 70
english = 60
ret = solution(korean, english)

print("solution 함수의 반환 값은", ret, "입니다.")
