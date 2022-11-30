# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution(shirt_size):
	answer = [0 for zero in range(6)]
	
	for size in shirt_size:
		
		if size == 'XS':
				answer[0] += 1
		elif size == 'S': 
			answer[1] += 1
		elif size == 'M':
			answer[2] += 1
		elif size == 'L':
			answer[3] += 1
		elif size == 'XL':
			answer[4] += 1
		elif size == 'XXL':
			answer[5] += 1
			
	return answer

if __name__ == '__main__':
  shirt_size = ["XS", "S", "L", "L", "XL", "S"]
  ret = solution(shirt_size);

  print("solution 함수의 반환 값은", ret, "입니다.")
