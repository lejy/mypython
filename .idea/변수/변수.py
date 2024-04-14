#문제 1~9정수 a를 받고 a + aa + aaa + aaaa 출력
a = int(input())
aa = a*11
aaa= a*111
aaaa= a*1111
sum = a+aa+aaa+aaaa
print(sum)