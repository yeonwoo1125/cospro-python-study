def solution(arr):
	answer = 0
	m = 0
	cnt = 1 # 증가의 시작점부터 카운트하기 위함
	
	for i in range(1, len(arr)):

		if arr[i - 1] < arr[i]:
			cnt += 1

		else:
			m = max(cnt, m)
			answer = m
			cnt = 1

	return answer

arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")
