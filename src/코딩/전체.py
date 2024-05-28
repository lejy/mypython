# 1부터 30까지 3, 6, 9 게임을 출력하는 코드입니다.
for i in range(1, 31):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print("짝!")
    else:
        print(i)


# a 까지 숫자
a = input()

for i in range(1,int(a)+1):
    if i < int(a):
        print(i, end=", ")
    else:
        print(i, end="")


# 입력값 바꾸기
a = list(input())
output = ""

for i in a:
    if i == " ":
        output += "링디기디기 \n"
    elif i == ".":
        output += "딩딩딩 \n"
    else:
        output += "링딩동 "
print(output)

