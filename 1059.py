# 문제
# 1059 : [기초-비트단위논리연산] 비트단위로 바꿔 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 21715  해결 문제 수: 17875
  
# 문제 설명    
# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.

# 입력
# 정수 1개가 입력된다.
# (-2147483648 ~ +2147483647)

# 출력
# 비트 단위로 1->0, 0->1로 바꾼후 그 값을 10진수로 출력한다.

# 입력 예시   
# 2

# 출력 예시
# -3

# 코드
a=int(input())
print(~a)