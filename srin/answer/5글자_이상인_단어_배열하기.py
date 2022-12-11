def solution(words):
	answer = ''
	
  # 단어의 길이가 5글자 이상이면 결과에 누적
	for word in words:
		if len(word) >= 5:
			answer+=word
	
  #결과값이 아무것도 없으면 empty 반환
	if len(answer) == 0:
		answer = 'empty'
	
	return answer

words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);

print("solution 함수의 반환 값은", ret1, "입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);

print("solution 함수의 반환 값은", ret2, "입니다.")
