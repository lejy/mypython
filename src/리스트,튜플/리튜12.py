# 콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.

a = input()
tup = ()
list = [x for x in a if x!= ',']
tup = tuple(x for x in a if x!=',')
print(list)
print(tup)