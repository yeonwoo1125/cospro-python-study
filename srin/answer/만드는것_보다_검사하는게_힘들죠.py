def solution(password):
	capital_count, small_count, digit_count = 0, 0, 0
	for p in password:
		if p >= 'A' and p <= 'Z':
			capital_count += 1
		elif p >= 'a' and p <= 'z':
			small_count += 1
		elif p >= '0' and p <= '9':
			digit_count += 1
	if capital_count >= 1 and small_count >= 2 and digit_count >= 2 :
		answer = True
	else:
		answer = False
	return answer

password1 = "helloworld"
ret1 = solution(password1)

print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "Hello123"
ret2 = solution(password2)

print("solution 함수의 반환 값은", ret2, "입니다.")
