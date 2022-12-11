def solution(words):
	answer = ''
	for word in words:
		if len(word) >= 5:
			answer += word
		
	if len(answer) == 0:
		answer = 'empty'
    
	return answer

if __name__ == '__main__':
  words1 = ["my", "favorite", "color", "is", "violet"]
  ret1 = solution(words1);

  print("solution 함수의 반환 값은", ret1, "입니다.")

  words2 = ["yes", "i", "am"]
  ret2 = solution(words2);

  print("solution 함수의 반환 값은", ret2, "입니다.")
