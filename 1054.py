# 문제
# 1054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 40121  해결 문제 수: 28261
  
# 문제 설명    
# 두 가지의 참(1) 또는 거짓(0)이 입력될 때,

# 모두 참일 때에만 참이 계산되는 프로그램을 작성해보자.

# 입력
# 1 또는 0의 값만 가지는 2개의 정수가 공백을 두고 입력된다.

# 출력
# 둘 다 참(1)일 경우에만 1을 출력하고 이외의 경우에는 0을 출력한다.

# 입력 예시   
# 1 1

# 출력 예시
# 1

# 코드
a,b=input().split()
if int(a)==1:
	if int(b)==1:
		print(1)
	else:
		print(0)
else:
	print(0)
