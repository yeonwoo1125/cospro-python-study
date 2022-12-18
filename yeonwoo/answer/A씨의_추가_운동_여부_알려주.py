def solution(calorie):
	min_cal = calorie[0]
	answer = 0
	for cal in calorie:
		if cal > min_cal:
			answer += cal - min_cal
		min_cal = min(min_cal, cal)
	return answer

if __name__ == '__main__':
  calorie = [713, 665, 873, 500, 751]
  ret = solution(calorie)

  # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
  print("solution 함수의 반환 값은", ret, "입니다.")
