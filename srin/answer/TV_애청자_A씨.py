def solution(programs):
	answer = 0
	used_tv = [0] * 25

	for program in programs:
		for i in range(program[0], program[1]):
			used_tv[i] = used_tv[i] + 1
			
	for i in used_tv:
		if i > 1:
			answer = answer + 1
	return answer

programs = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)

print("solution 함수의 반환 값은", ret, "입니다.")
