# 문제
# 1081 : [기초-종합] 주사위를 2개 던지면?
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 31057  해결 문제 수: 18618

# 문제 설명    
# 1부터 n까지, 1부터 m 까지 숫자가 적힌 색이 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력해보자.

# 입력
# 서로 다른 주사위의 면의 개수 n, m이 공백을 두고 입력된다.
#  (단, n, m은 10이하의 자연수)

# 출력
# 나올 수 있는 주사위의 숫자가 한 세트씩 줄을 바꿔 모두 출력된다.
# 첫 수는 n, 두번째 수는 m으로 고정해 출력하도록 한다.

# 입력 예시   
# 2 3

# 출력 예시
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3

# 코드
a,b=input().split()
a=int(a)
b=int(b)
for i in range(1,a+1):
	for j in range(1,b+1):
		print(i,j)