def solution(calorie):
	min_cal = calorie[0]
	answer = 0
	for cal in calorie:
		if cal > min_cal:
			answer += cal - min_cal
		min_cal = min(min_cal, cal)
	return answer


calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)

print("solution 함수의 반환 값은", ret, "입니다.")
