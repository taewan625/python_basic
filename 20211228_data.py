# 주석 설명
# 컴퓨터 프로그램 할 때 각종 데이터들이 있다
# 숫자, 문자, 등등 존재 -> 기본적으로 처리시 기억장소에 넣는다. = 변수
# 형식: 변수이름 정의 = 데이터
a = 100 # 숫자  해석: a라는 기억장소에 숫자 100 입력
print(a) # 100이 출력됨

# print(5)

a = a * 100 # 오른쪽에 있는 계산을 수행하고 오른쪽 변수에 지참 
# a <- 100*100
print(a) # a에 있는 내용을 터미널에 출력하세요라는 함수, (내장)함수 *5번줄에 a 값을 지정했지만 8번에 재정의하여서 print 될 때 10000 값이 출력된다.

# 한줄 주석_visual studio code. win: ctrl + / , mac: command + / ; 마우스로 원하는 범위 지정하여 주석 풀기 및 첨가 가능
'''
여러줄 주석
'''

# 제곱 2^3 -> 2*2*2
a = 100   # 변수사용 ,, 재사용
b = 2**a  # 2를 a 만큼 제곱해라 의미
# b= 2**3 # 2의 3 제곱값을 b 라는 기억장소에 저장
print(b)

#  변수 사용 예
a = '영문과' # 학과 데이터
# 문자열 출력 방법1 : comma , 
print(a, '학생입니다') # '' 안에는 문자열

# 실습문제
# 버스 정류소
# 365번 버스가 잠시 후 도착합니다.
# 336번 버스가 잠시 후 도착합니다.
# 270번 버스가 잠시 후 도착합니다.
a = '365번'
print(a, '버스가 잠시 후 도착합니다')