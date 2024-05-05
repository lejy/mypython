# 다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.

a = input()
b = []
c = 2
for i in a:
    if c %2 == 0:
        b.append(i)
    c += 1
print(''.join(b))