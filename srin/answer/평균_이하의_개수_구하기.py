def solution(data):
	total = sum(data)
	average = total/len(data)
	cnt = 0
	for d in data:
		if d <= average:
			cnt += 1
	return cnt

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution(data1)

print("solution 함수의 반환 값은", ret1, "입니다.")

data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)

print("solution 함수의 반환 값은", ret2, "입니다.")
