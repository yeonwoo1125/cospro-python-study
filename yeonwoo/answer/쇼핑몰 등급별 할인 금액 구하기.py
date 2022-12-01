# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(price, grade):
	answer = 0

	if grade == 'V':
		discount = 85/100
	elif grade =='G':
		discount = 90/100
	elif grade == 'S':
		discount = 95/100
		
	answer = int(price * discount)
	
	return answer

if __name__ == '__main__':
  price1 = 2500
  grade1 = "V"
  ret1 = solution(price1, grade1)
  
  print("solution 함수의 반환 값은", ret1, "입니다.")
      
  price2 = 96900
  grade2 = "S"
  ret2 = solution(price2, grade2)
  
  print("solution 함수의 반환 값은", ret2, "입니다.")
