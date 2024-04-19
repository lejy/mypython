# 주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.

tup = (1,2,3,4,5,6,7,8,9,10)
mid = int(tup[9]/2)
tup1 = tuple(tup[:mid])
tup2 = tuple(tup[mid:])
print(tup1)
print(tup2)
