# 문제
# 1084 : [기초-종합] 물감만들기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 24175  해결 문제 수: 14337

# 문제 설명    
# 빨강(red), 녹색(green), 파랑(blue) 물감을 섞어 여러 가지 물감을 만들어 내려고한다.
# 빨강(r), 녹색(g), 파랑(b) 물감의 종류(농도에 따라 0~ n-1 까지 n가지의 농도를 만들 수 있다.)가 주어질 때,
# 주어진 물감들을 농도를 다르게 섞어 만들 수 있는 모든 물감의 정보(r g b)와 그 최대 개수를 계산해보자.

# 입력
# 빨녹파(r, g, b) 각 물감의 종류(농도) 개수가 공백을 사이에 두고 입력된다.
# (0 ~ 128)
# 예를 들어 3 3 3 은 각 색에 대해서 0~2까지 3가지 물감이 있음을 의미한다.

# 출력
# 만들 수 있는 물감의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로 줄을 바꿔 모두 출력하고,
# 마지막에 그 개수를 출력한다.

# 입력 예시   
# 2 2 2

# 출력 예시
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
# 8 

# 코드
a,b,c=input().split()
num=0
for i in range(0,int(a)):
	for j in range(0,int(b)):
		for k in range(0,int(c)):
			print(i,j,k)
			num+=1
print(num)
