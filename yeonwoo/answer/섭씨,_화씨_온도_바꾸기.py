def solution(value, unit):
	converted = 0
	if unit == "C":
		value = value * 1.8 + 32
	if unit == "F":
		value = (value - 32) / 1.8
	converted = int(value)
	return converted

if __name__ == '__main__':
  value = 527
  unit = "C"
  ret = solution(value, unit)

  print("solution 함수의 반환 값은", ret, "입니다.")

  value = 980
  unit = "F"
  ret = solution(value, unit)

  print("solution 함수의 반환 값은", ret, "입니다.")
