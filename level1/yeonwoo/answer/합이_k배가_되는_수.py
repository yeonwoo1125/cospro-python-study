def solution(arr, K):
	answer = 0
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			for k in range(j+1, len(arr)):

				if (arr[i] + arr[j] + arr[k]) % k == 0:
					answer += 1
					
	return answer

arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")
