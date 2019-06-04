# 문제
# 1070 : [기초-조건/선택실행구조] 달 입력 받아 계절 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 45100  해결 문제 수: 26430
  
# 문제 설명    
# 월이 입력될 때 계절이 출력되도록 해보자.

# 예
# 월 : 계절
# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall

# 입력
# 월을 의미하는 한 개의 정수가 입력된다.
# (1 ~ 12)

# 출력
# 계절을 출력한다.

# 입력 예시   
# 12

# 출력 예시
# winter

# 코드
a=int(input())
if 2<a<6:
	print('spring')
elif 5<a<9:
	print('summer')
elif 8<a<12:
	print('fall')
else:
	print('winter')
	
