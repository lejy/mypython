# 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
# 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.


def pal(a):
    b = ''
    for i in a:
        b = i + b
    if b==a:
        print("입력하신 단어는 회문(Palindrome)입니다.")

a = str(input())
pal(a)


