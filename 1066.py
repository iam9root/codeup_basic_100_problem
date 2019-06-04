# 문제
# 1066 : [기초-조건/선택실행구조] 정수 세 개 입력받아 짝/홀 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 58185  해결 문제 수: 34568
  
# 문제 설명    
# 세 정수 a, b, c가 입력되었을 때,
# 짝 even(짝)/odd(홀)을 출력해보자.

# 입력
# 세 정수 a, b, c 가 공백을 두고 입력된다.
# (0 ~ 2147483647)

# 출력
# 순서대로 even(짝)/odd(홀)을 줄을 바꿔 출력한다.

# 입력 예시   
# 1 2 8

# 출력 예시
# odd
# even
# even

# 코드
a,b,c=input().split()
print('even') if int(a)%2==0 else print('odd')
print('even') if int(b)%2==0 else print('odd')
print('even') if int(c)%2==0 else print('odd')
