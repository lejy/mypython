def analyze_text(words):
    # 키워드, 해시태그, 멘션을 저장할 리스트를 각각 생성합니다.
    keywords, hashtags, mentions = [], [], []

    for i in words:
        if i.startswith("@"):
            mentions.append(i[1:])
        elif i.startswith("#"):
            hashtags.append(i[1:])
        else:
            keywords.append(i)

    return keywords, hashtags, mentions


test=["#hello","@mention","origin"]

print(analyze_text(test))