# 문제
# 1069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 54111  해결 문제 수: 25696
  
# 문제 설명    
# 평가(A, B, C, D, ...)를 문자로 입력 받아 내용을 다르게 출력해보자.
# 평가내용
# 평가 : 내용
# D : slowly~
# C : run!
# B : good!!
# A : best!!!
# 나머지문자들 : what?

# 입력
# 영문자 한 개가 입력된다.
# (A, B, C, D 등의 문자가 입력된다.)

# 출력
# 평가내용에 따라 다른 내용이 출력된다.

# 입력 예시   
# A

# 출력 예시
# best!!!

# 코드
a=input()
if a=='A':
	print('best!!!')
elif a=='B':
	print('good!!')
elif a=='C':
	print('run!')
elif a=='D':
	print('slowly~')
else:
	print('what?')
	
