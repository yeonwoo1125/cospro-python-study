# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(arr):
	left, right = 0, len(arr)-1
	while right != 1:
		arr[left], arr[right] = arr[right], arr[left]
		left += 1
		right -= 1
	return arr


if __name__ == '__main__':
  arr = [1, 4, 2, 3]
  ret = solution(arr)

  print("solution 함수의 반환 값은", ret, "입니다.")
