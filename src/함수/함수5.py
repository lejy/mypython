# 리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
# 이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.

list = [1,2,3,4,3,2,1]

def unique(a):
    new = []
    for i in a:
        if i not in new:
            new.append(i)
    print(new)

unique(list)
