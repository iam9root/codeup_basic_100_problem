# 문제

# 1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 28328  해결 문제 수: 22032
  
# 문제 설명    
# 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
# (단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.)

# 입력
# 두 정수가 공백을 두고 입력된다.
# (-2147483648 ~ 2147483647)

# 출력
# 큰 값이 10진수로 출력된다.

# 입력 예시   
# 123 456

# 출력 예시
# 456

# 코드
a,b=input().split()
a=int(a)
b=int(b)
r=a if a>b else b
print(r)