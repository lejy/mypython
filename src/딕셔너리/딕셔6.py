# 다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.

a = input()
LETTERS = 0
DIGITS = 0

for x in a:
    if 48 <= ord(x) <= 57:
        DIGITS += 1
    elif 65 <= ord(x.upper()) <= 90:
        LETTERS += 1

print(f"LETTERS {LETTERS}")
print(f"DIGITS {DIGITS}")
