# 문제
# 1051 : [기초-비교연산] 두 정수 입력받아 비교하기3
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 41653  해결 문제 수: 32057
  
# 문제 설명    
# 두 정수(a, b)를 입력받아,
# b가 a보다 크거나 같으면 1, b가 a보다 작으면 0
# 을 출력하는 프로그램을 작성해보자.
# 입력
# 두 정수 a, b가 공백을 두고 입력된다.

# (-2147483648 ~ 2147483647)

# 출력
# b가 a보다 크거나 같은 경우 1, 그렇지 않은 경우 0을 출력한다.

# 입력 예시   
# 0 -1

# 출력 예시
# 0

# 코드
a,b=input().split()
if a<=b:
	print(1)
else:
	print(0)
