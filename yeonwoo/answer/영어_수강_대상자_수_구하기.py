# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(scores):
	count = 0
	for s in scores:
		if s >= 650 and s < 800:
			count += 1
	return count

if __name__ == '__main__':
  scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
  ret = solution(scores)

  print("solution 함수의 반환 값은", ret, "입니다.")
