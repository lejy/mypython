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

# 단어어 해당 단어의 빈도수를 담은 리스트를 선언합니다. 수정하지 마세요.
pairs = [
    ('time', 8),
    ('the', 15),
    ('turbo', 1),
]

#(단어, 빈도수) 쌍으로 이루어진 튜플을 받아, 빈도수를 리턴합니다.
def get_freq(pair):


    return pair[1]



#(단어, 빈도수) 꼴 튜플의 리스트를 받아, 빈도수가 낮은 순서대로 정렬하여 리턴합니다.
def sort_by_frequency(pairs):

    return sorted(pairs,key = get_freq)


# 아래 주석을 해제하고 결과를 확인해보세요.
print(sort_by_frequency(pairs))
