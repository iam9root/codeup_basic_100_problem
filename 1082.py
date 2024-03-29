# 문제
# 1082 : [기초-종합] 16진수 구구단?
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 31245  해결 문제 수: 13865

# 문제 설명    
# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운 경곽이는
# 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.
# A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
# (단, A ~ F 까지만 입력된다.)

# 입력
# 16진수로 한자리 수가 입력된다.
# (단, A ~ F 까지만 입력된다.)

# 출력
# 입력한 16진수에 1~F까지 순서대로 곱한,
# 16진수 구구단을 줄을 바꿔 출력한다.
# 계산 결과도 16진수로 출력해야 한다.

# 입력 예시   
# B

# 출력 예시
# B*1=B
# B*2=16
# B*3=21
# B*4=2C
# B*5=37
# B*6=42
# B*7=4D
# B*8=58
# B*9=63
# B*A=6E
# B*B=79
# B*C=84
# B*D=8F
# B*E=9A
# B*F=A5

# 코드
a=int(input(),16)
for i in range(1,16):
	print(str(hex(a))[2:].upper()+'*'+str(hex(i))[2:].upper()+'='+str(hex((a*i)))[2:].upper())
