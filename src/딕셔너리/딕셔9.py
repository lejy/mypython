# 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.

a = list(input())
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in dic:
    print(f"{i},{dic[i]}")


