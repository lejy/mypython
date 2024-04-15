#2진수 변환

b = []
a = int(input())

while a > 0:
    b.append(a % 2)
    a //= 2

for i in range(len(b) - 1, -1, -1):
    print(b[i], end="")
