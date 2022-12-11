def solution(N, M):
	answer = 0
	for i in range(N, M):
		if i % 2 == 0:
			answer += i ** 2
	return answer

if __name__ == '__main__':
  N = 4
  M = 7
  ret = solution(N, M)

  print("solution 함수의 반환 값은", ret, "입니다.")
