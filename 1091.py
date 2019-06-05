# 문제
# 1091 : [기초-종합] 수 나열하기3
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 18386  해결 문제 수: 12048

# 문제 설명    
# 어떤 규칙에 따라 수를 순서대로 나열한 것을 수열이라고 한다.
# 예를 들어 
# 1 -1 3 -5 11 -21 43 ... 은 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.

# 이런 이상한 수열을 알게 된 경곽이는 또 궁금해 졌다.
# "그럼.... 13번째 나오는 수는 뭘까?"
# 경곽이는 물론 수학을 아주 잘 하지만 이런 문제는 본적이 거의 없었다...
# 그래서, 프로그램을 만들어 컴퓨터로 확인해 보고 싶어졌다. 

# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가 입력될 때,
# n번째 수를 출력하는 프로그램을 만들어보자.

# 입력
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가 공백을 두고 입력된다.
# (a, m, d는 -50 ~ 50, n은 10이하의 자연수)

# 출력
# n번째로 만들어질 수를 출력한다.

# 입력 예시   
# 1 -2 1 8

# 출력 예시
# -85

# 코드
a,b,c,d=input().split()
sum=int(a)
for i in range(0,int(d)-1):
	sum=sum*int(b)+int(c)
print(sum)
