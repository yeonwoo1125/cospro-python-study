# 제곱을 사용하기 위해 math module을 import
import math

def solution(N, M):
	answer = 0
  # N~M 범위 중 짝수인 값에 대해 제곱하여 answer에 누적
	for number in range(N, M):
		if number % 2 == 0:
			answer += math.pow(number, 2)
	return int(answer)

N = 4
M = 7
ret = solution(N, M)

print("solution 함수의 반환 값은", ret, "입니다.")
