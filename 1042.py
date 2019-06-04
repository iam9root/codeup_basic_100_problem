# 문제
# 1042 : [기초-산술연산] 정수 두 개 입력받아 나눈 몫 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 62228  해결 문제 수: 37477

# 문제 설명    
# 정수 두 개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력하는 프로그램을 작성해보자.
# (단, 입력되는 두 개의 정수 a, b의 범위는 -2147483648 ~ 2147483647이고, b는 0이 아니다.)

# 입력
# 정수 두 개(a, b)가 공백을 두고 입력된다.
# (단, a, b의 범위는 -2147483648 ~  2147483647이고, b는 0이 아니다.)

# 출력
# a를 b로 나누었을 때의 몫을 정수형태로 출력한다. 

# 예를 들어 5÷2=2.5 인경우, 2를 출력한다.

# 입력 예시   
# 1 3

# 출력 예시
# 0

# 코드
a,b=input().split()
print(int(a)//int(b))