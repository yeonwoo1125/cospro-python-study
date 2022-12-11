def solution(floors):
	dist = 0
	length = len(floors)
  
  # for문 내에 i-1을 사용하므로 범위는 1~floors배열의 크기만큼이다.
	for i in range(1, length):
    # 만약, 현재 층수가 이전 층수보다 크면 (현재층수)-(이전층수)
		if floors[i] >= floors[i-1]:
			dist += floors[i] - floors[i-1]
      
    # 아니면 (이전층수)-(현재층수)로 계산한다.
		else:
			dist += floors[i-1] - floors[i]
	return dist


floors = [1, 2, 5, 4, 2]
ret = solution(floors)

print("solution 함수의 반환 값은", ret, "입니다.")
