def solution(socks):
	answer = 0
	count = [0 for _ in range(10)]
	for s in socks:
		count[s] += 1
		
	for c in count:
		answer += (c // 2)
	return answer

socks = [1, 2, 1, 3, 2, 1]
ret = solution(socks)

print("solution 함수의 반환 값은", ret, "입니다.")
