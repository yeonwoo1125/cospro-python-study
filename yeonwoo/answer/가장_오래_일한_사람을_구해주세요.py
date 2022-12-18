def solution(time_table, n):
	answer = 0
	a = [ 0 for i in range(n)]
	for i, t in enumerate(time_table):
		a[i % n] += time_table[i]
		
	answer = a[0]
	for t in a:
		answer = max(t, answer)
		
	return answer

if __name__ == '__main__':
  time_table1 = [1, 5, 1, 9]
  n1 = 3
  ret1 = solution(time_table1, n1)

  print("solution 함수의 반환 값은", ret1, "입니다.")

  time_table2 = [4, 8, 2, 5, 4, 6, 7]
  n2 = 4
  ret2 = solution(time_table2, n2)

  print("solution 함수의 반환 값은", ret2, "입니다.")
