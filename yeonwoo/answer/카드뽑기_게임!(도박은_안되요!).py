def solution(cards):
	answer = 0
	count = {}
	
	for i in range(len(cards)):
		card = cards[i][0]
		if card in count:
			count.update({card : count.get(card) + 1})
		else:
			count.update({card : 0})
	
	for i in range(len(cards)):
				answer += int(cards[i][1])
	
	d = 0
	for cnt in count.values():
		d = max(cnt, d)

	if d == 1:
		answer *= 2
	elif d == 2:
		answer *= 3
		
	return answer

if __name__ == '__main__':
  cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
  ret1 = solution(cards1)

  print("solution 함수의 반환 값은", ret1, "입니다.")

  cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
  ret2 = solution(cards2)

  print("solution 함수의 반환 값은", ret2, "입니다.")
