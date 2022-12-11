def solution(votes, N, K):
	counter = [0 for _ in range(N + 1)]
	for x in votes:
		counter[x] += 1
    
  # 반환되는 변수인 answer의 초기값은 0이어야한다.
	answer = 0
	for c in counter:
		if c == K:
			answer += 1
	return answer


votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N = 5
K = 2
ret = solution(votes, N, K)

print("solution 함수의 반환 값은", ret, "입니다.")
