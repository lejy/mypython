# 다음의 결과와 같이 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램을 작성합니다.
# 아무 것도 입력하지 않고 엔터만 입력하면 입력이 종료됩니다.
a = []
now = 'd'
while now != '':
    now = input()
    a.append(now)

a.pop()

for i in a:
    print(">>", i.upper())
