# 문제
# 1068 : [기초-조건/선택실행구조] 정수 한 개 입력받아 평가 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 52055  해결 문제 수: 30506
  
# 문제 설명    
# 점수(정수)를 입력받아 평가를 출력해보자.
# (0 ~ 100)
# 평가기준
# 점수범위 : 평가
# 90 ~ 100 : A
# 70 ~ 89 : B
# 40 ~ 69 : C
# 0 ~ 39 : D
# 로 평가되어야 한다.

# 입력
# 정수 한 개가 입력된다.
# (0 ~ 100)

# 출력
# 평가 기준에 따라, 평가가 문자로 출력된다.

# 입력 예시   
# 90

# 출력 예시
# A

# 코드
a=int(input())
if a>39:
	if a>69:
		if a>89:
			print('A')
		else:
			print('B')
	else:
		print('C')
else:
	print('D')
