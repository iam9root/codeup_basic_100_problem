# 문제
# 1065 : [기초-조건/선택실행구조] 정수 세 개 입력받아 짝수만 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 69731  해결 문제 수: 37722
  
# 문제 설명    
# 세 정수 a, b, c가 입력되었을 때,
# 짝수만 출력해보자.

# 입력
# 세 정수 a, b, c 가 공백을 두고 입력된다.
# (0 ~ 2147483647 범위의 정수들이 입력되며, 적어도 1개는 짝수이다.)

# 출력
# 짝 수만 순서대로 줄을 바꿔 출력한다.

# 입력 예시   
# 1 2 4

# 출력 예시
# 2
# 4

# 코드
a,b,c=input().split()
if int(a)%2==0:
	print(a)
if int(b)%2==0:
	print(b)
if int(c)%2==0:
	print(c)
