# 문제
# 1076 : [기초-반복실행구조] 문자 한 개 입력받아 알파벳 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 49311  해결 문제 수: 21325
  
# 문제 설명    
# 영문자 한 개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.
# (a ~ z)

# 입력
# 영문자 한 개가 입력된다.
# (a ~ z)

# 출력
# a부터 입력한 문자까지 순서대로 공백을 두고 출력된다.

# 입력 예시   
# f

# 출력 예시
# a b c d e f

# 코드
a=ord(input())
for i in range(97,a+1):
	print(chr(i),end=' ')
