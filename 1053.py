# 문제
# 1053 : [기초-논리연산] 참 거짓 바꾸기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 37860  해결 문제 수: 27407
  
# 문제 설명    
# 1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때
# 반대로 출력하는 프로그램을 작성해보자.

# 입력
# 정수 1개가 입력된다.
# (단, 0 또는 1 만 입력된다.)

# 출력
# 입력된 값이 0이면 1, 1이면 0을 출력한다.

# 입력 예시   
# 1

# 출력 예시
# 0

# 코드
a=int(input())
if a==1:
	print(0)
else:
	print(1)
