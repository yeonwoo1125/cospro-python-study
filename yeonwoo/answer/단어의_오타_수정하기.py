def solution(words, word):
	count = 0
	for w in words:
		if not w == word: # COED, CODE
			for j, c in enumerate(w):
				if not c == word[j]: # E, D
					count += 1 

	return count

if __name__ == '__main__':
  words = ["CODE", "COED", "CDEO"]
  word = "CODE"
  ret = solution(words, word)

  print("solution 함수의 반환 값은", ret, "입니다.")
