# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(sentence):
	str = ''
	for c in sentence:
		if c != '.' and c != ' ':
			str += c
	size = len(str)
	for i in range(size // 2):
		if str[i] != str[size - 1 - i]:
			return False
	return True

if __name__ == '__main__':
  sentence1 = "never odd or even."
  ret1 = solution(sentence1)

  print("solution 함수의 반환 값은", ret1, "입니다.")

  sentence2 = "palindrome"
  ret2 = solution(sentence2)

  print("solution 함수의 반환 값은", ret2, "입니다.")
