def solution(purchase):
	total = 0
	for p in purchase:
		if p >= 1000000:
			total += 50000
		elif p >= 600000:
			total += 30000
		elif p >= 400000:
			total += 20000
    # 문제의 조건에 40만원 미만인 고객 모두가 아닌, 20만원 이상인 고객에게만
    # 상품권 10000원을 지급한다고 나와있다.
		elif p >= 200000:
			total += 10000
	return total
  
  
purchase = [150000, 210000, 399990, 990000, 1000000]
ret = solution(purchase)

print("solution 함수의 반환 값은", ret, "입니다.")
