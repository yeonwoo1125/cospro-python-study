def solution(value, unit):
	converted = 0
	if unit == "C":
		value = value * 1.8 + 32
	if unit == "F":
    # 연산자 우선순위에 의해 (/)부호가 (-)부호보다 먼저 실행되므로, 
    # (괄호)를 통해 (-)의 우선순위를 높여주어야한다.
		value = (value - 32) / 1.8
	converted = int(value)
	return converted


value = 527
unit = "C"
ret = solution(value, unit)

print("solution 함수의 반환 값은", ret, "입니다.")

value = 980
unit = "F"
ret = solution(value, unit)

print("solution 함수의 반환 값은", ret, "입니다.")
