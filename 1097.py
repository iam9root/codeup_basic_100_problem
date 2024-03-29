# 문제
# 1097 : [기초-종합+배열] 바둑알 십자 뒤집기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 21707  해결 문제 수: 8157

# 문제 설명    
# 아버지를 기다리던 경곽이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

# "음... 이거... 십(+)자 뒤집기를 해볼까?"하고 생각하였다.

# 바둑판(19×19)에 흰돌(1)/검정돌(0) 모두 꽉 채워놓여있을 때,

# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

# 입력
# 바둑알이 깔려 있는 상황이 19×19 로 입력된다.
# 십자바꾸기 횟수(n)가 입력된다.
# 십자바꾸기 좌표가 횟수(n) 만큼 입력된다. 
# 단, n은 10이하의 자연수이다.

# 출력
# 십자 바꾸기 결과를 출력한다.

# 입력 예시   
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0
# 2
# 10 10
# 12 12

# 출력 예시
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 코드
baduk=[[0]*19 for i in range(19)]
for i in range(0,19):
	a=input().split()
	for j in range(0,19):
		baduk[i][j]=a[j]
num=int(input())
for i in range(0,num):
	a,b=input().split()
	a=int(a)
	b=int(b)
	for j in range(0,19):
		if baduk[a-1][j]=='1':
			baduk[a-1][j]=0
		# elif baduk[a-1][j]=='0':
		else:
			baduk[a-1][j]=1
		if baduk[j][b-1]=='1':
			baduk[j][b-1]=0
		# elif baduk[j][b-1]=='0':
		else:
			baduk[j][b-1]=1
for i in range(0,19):
	for j in range(0,19):
		print(baduk[i][j], end=' ')
	print('')
