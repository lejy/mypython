# 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
# 이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.

list = [2,4,6,8,10]

def check(a,b):
    if a in b:
        print(f"{a} => True")
    else:
        print(f"{a} => False")
print(list)
check(5,list)
check(10,list)