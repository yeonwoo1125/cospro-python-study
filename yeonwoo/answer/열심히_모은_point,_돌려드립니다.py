import math

def solution(point):
	if point < 1000:
		return 0
	return math.trunc(point / 100) * 100

if __name__ == '__main__':
  point = 2323
  ret = solution(point)

  print("solution 함수의 반환 값은", ret, "입니다.")
