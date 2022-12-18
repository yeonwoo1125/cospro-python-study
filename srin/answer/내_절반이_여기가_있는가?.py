def solution(arr):
	answer = 0
	for i in arr:
		if i/2 in arr:
			answer += 1
	return answer

arr = [4, 8, 3, 6, 7]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")
