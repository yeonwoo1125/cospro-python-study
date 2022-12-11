def solution(number):
	count = 0
  # number가 0보다 클동안 while문을 진행
  # 0이 같을때도 while문을 돌리게하면, 무한 루프에 빠지게 된다.(나누어서 0보다 미만의 수가 나올 수 없기 때문)
	while number > 0:
		n = number % 10
		if n == 2 or n == 3 or n == 5 or n == 7:
			count += 1
    # (//=)연산자는 python에서 나머지가 없는 나누기 결과값을 반환함
		number //= 10
	return count
  
number = 29022531
ret = solution(number)

print("solution 함수의 반환 값은", ret, "입니다.")
  
