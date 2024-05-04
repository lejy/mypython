# 다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.



a = "A better tomorrow"

b = ' '.join(a.split()[::-1])

print(b)
