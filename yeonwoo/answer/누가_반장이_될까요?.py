def solution(n, votes):
	answer = 0
	votes_len = len(votes)
	candidate = votes[0]
	count = 1
	for i in range (1, votes_len) :
		if candidate == votes[i] :
			count += 1
		else :
			count -= 1
		if count == 0 :
			candidate = votes[i]
			count = 1

	test_count = 0
	for i in range(0, votes_len) :
		if votes[i] == candidate :
			test_count += 1

	if test_count > votes_len // 2 :
		answer = candidate
	else :
		answer = -1

	return answer

if __name__ == '__main__':
  n1 = 3
  votes1 = [1, 2, 1, 3, 1, 2, 1]
  ret1 = solution(n1, votes1)

  print("solution 함수의 반환 값은", ret1, "입니다.")

  n2 = 2
  votes2 = [2, 1, 2, 1, 2, 2, 1]
  ret2 = solution(n2, votes2)

  print("solution 함수의 반환 값은", ret2, "입니다.")
