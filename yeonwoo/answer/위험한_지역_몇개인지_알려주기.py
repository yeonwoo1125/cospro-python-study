def solution(height):
	count = 0
	leng = len(height)
	for i in range(leng):
		for j in range(leng):
			if i > 0 and height[i][j] > height[i-1][j]:
				pass
			elif i < leng - 1 and height[i][j] > height[i+1][j]:
				pass
			elif j > 0 and height[i][j] > height[i][j-1]:
				pass
			elif j < leng - 1 and height[i][j] > height[i][j+1]:
				pass
			else:
				count += 1
				
	return count

if __name__ == '__main__':
  height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
  ret = solution(height)

  print("solution 함수의 반환 값은", ret, "입니다.")
