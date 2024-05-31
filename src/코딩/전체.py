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




def preprocess_data(filename):
    processed = {}
    with open(filename) as file:
        # 입력 받은 JSON 파일을 불러와 loaded에 저장합니다.
        loaded = json.loads(file.read())
        # JSON 형식의 데이터에서 영화와 사용자 정보를 하나씩 가져옵니다.
        for movie, user in loaded.items():
            processed[int(movie)] = user
            # processed 딕셔너리에 title을 키로, user를 값으로 저장합니다.


        return processed


def reformat_data(title_to_users):
    user_to_titles = {}
    # 입력받은 딕셔너리에서 영화와 사용자 정보를 하나씩 가져옵니다.
    for movie,user in title_to_users.items():
        # user_to_titles에 사용자 정보가 있을 경우 사용자의 영화 정보를 추가합니다. 이때 영화 정보는 리스트형으로 저장됩니다.
        for use in user:
            if use in user_to_titles:  # 사용자 정보가 이미 딕셔너리에 존재하는 경우 해당 사용자의 영화 정보를 추가
                user_to_titles[use].append(movie)
            else:  # 사용자 정보가 없는 경우 새로운 사용자 정보로 키를 추가하고 영화 정보를 리스트로 저장
                user_to_titles[use] = [movie]

    return user_to_titles


def get_closeness(title_to_users, title1, title2):
    # title_to_users를 이용해 title1를 시청한 사용자의 집합을 저장합니다.
    title1_users = set(title_to_users[title1])
    # title_to_users를 이용해 title2를 시청한 사용자의 집합을 저장합니다.
    title2_users = set(title_to_users[title2])

    # 두 작품을 모두 본 사용자를 구합니다.
    both = len(title1_users & title2_users)
    # 두 작품 중 하나라도 본 사용자를 구합니다.
    either = len(title1_users | title2_users)

    return both / either


def predict_preference(title_to_users, user_to_titles, user, title):
    # user_to_titles를 이용해 user가 시청한 영화를 저장합니다.


    titles = user_to_titles[user]
    closeness = [get_closeness(title_to_users, title, title2) for title2 in titles]
    return sum(closeness) / len(closeness)
