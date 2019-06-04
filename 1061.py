# 문제
# 1061 : [기초-비트단위논리연산] 비트단위로 xor 하여 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 21476  해결 문제 수: 17418

# 문제 설명    
# 입력 된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.

# 입력
# 두 개의 정수가 공백을 두고 입력된다.
# (-2147483648 ~ 2147483647)

# 출력
# 두 정수를 비트단위로 xor 계산을 수행한 결과가 10진수로 출력된다.

# 입력 예시   
# 3 5

# 출력 예시
# 6

# 코드
a,b=input().split()
print(int(a)^int(b))
