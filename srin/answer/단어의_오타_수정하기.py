def solution(words, word):
	count = 0
	for value in words:
		if value!=word :
			for i in range(len(value)) :
				if value[i]!=word[i] :
					count+=1
	return count

words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

print("solution 함수의 반환 값은", ret, "입니다.")
