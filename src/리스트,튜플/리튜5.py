# 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.
a = []
a.append(int(input()))
out =[]
for i in range(1,a[0]):
    if a[0] % i == 0:
        out.append(i)
print(out)