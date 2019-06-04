# 문제
# 1027 : [기초-입출력] 년월일 입력받아 형태 바꿔 출력하기
# 시간 제한: 1 Sec  메모리 제한: 128 MB
# 제출: 59752  해결 문제 수: 33391

# 문제 설명    
# 년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.
# 날짜를 년월일(yyyy.mm.dd)의 형태로 입력받아,
# 일월년(dd-mm-yyyy)의 형태로 출력하는 프로그램을 작성해보자.
# (단, 한 자리 일/월은 0을 붙여 두 자리로, 년도는 0을 붙여 네 자리로 출력한다.)

# 입력
# 년월일이 '.'(닷)으로 구분되어 입력된다.

# 출력
# 년월일을

# 일월년으로 바꾸어 '-'(대쉬, 마이너스)로 구분해 출력한다.

# 입력 예시   
# 2014.07.15

# 출력 예시
# 15-07-2014

# 코드
yyyy,mm,dd=input().split('.')
print(dd.zfill(2)+'-'+mm.zfill(2)+'-'+yyyy)