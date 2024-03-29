# 문제
# 1092 : [기초-종합] 함께 문제 푸는 날1
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 19076  해결 문제 수: 12418

# 문제 설명    
# koistudy.net 에는
# 초등학생, 중학생, 고등학생, 대학생, 대학원생, 일반인, 군인, 프로그래머, 탑코더  등 아주 많은 사람들이 들어와 문제를 풀고 있는데, 가입하고 Guest Board를 통해 정회원으로 등업이 되어야 문제를 풀어볼 수 있다.
# 매 시간의 실시간 채점 정보는 메뉴의 Judge Status 를 통해 살펴볼 수 있다.

# 자! 여기서...잠깐..
# 같은 날 동시에 가입한 3명의 사람들이 koistudy.net을 들어와 문제를 푸는 날짜가
# 매우 규칙적이라고 할 때,
# 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?
# 예를 들어 3명이 같은날 가입/등업하고, 각각 3일 마다, 7일 마다, 9일 마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

# 입력
# 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는, 방문 주기가 공백을 두고 입력된다.
#  (단, 입력값은 100이하의 자연수이다.)

# 출력
# 3명이 다시 모두 함께 방문에 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?) 을 출력한다.

# 입력 예시   
# 3 7 9

# 출력 예시
# 63

# 코드
a,b,c=input().split()
max_value=max(int(a),int(b),int(c))
while 1:
	if max_value%int(a)==0 and max_value%int(b)==0 and max_value%int(c)==0:
		print(max_value)
		break
	max_value+=1
