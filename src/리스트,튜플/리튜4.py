# 리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.

a = []

for i in range(0,5):
    a.append(int(input()))

print(sum(a)/len(a))
