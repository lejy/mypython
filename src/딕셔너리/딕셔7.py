# 다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.
a = input()
up = 0
low = 0

for x in a:
    if 97 <= ord(x) <= 122:
        low += 1
    elif 65 <= ord(x) <= 90:
        up += 1

print(f"UPPER CASE {up}")
print(f"LOWER CASE {low}")
