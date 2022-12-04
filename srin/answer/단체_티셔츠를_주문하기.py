def solution(shirt_size):
	answer = [0, 0, 0, 0, 0, 0]
	for i in shirt_size :
		idx = 0;
		
		if i=="XS" : 
			idx = 0
		elif i=="S" : 
			idx = 1
		elif i == "M" :
			idx = 2
		elif i == "L" :
			idx = 3
		elif i == "XL" :
			idx = 4
		elif i == "XXL" :
			idx = 5
			
		answer[idx]+=1
	return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)

print("solution 함수의 반환 값은", ret, "입니다.")
