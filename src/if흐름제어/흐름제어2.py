# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
# (단, 약수가 2개일 경우 소수임을 나타내십시오)

a = int(input())
b = []
count = 0
for i in range(1,a+1):
    if(a % i == 0):
        print("%d는 %d의 약수입니다."% (i,a))
        b.append(i)

if len(b) == 2:
    print("%d는 %s로 나눠지는 소수임" % (a, b))


