# 다음 두 딕셔너리 객체를 합쳐 중복된 메뉴가 없는 딕셔너리를 만들고
# 가격이 3000원 이상인 메뉴를 아래와 같이 출력하는 프로그렘을 작성하십시오.
# 중복된 메뉴의 가격이 다를 경우 딕셔너리 a의 가격을 사용하세요.
# a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
# b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

new = {}
new2={}
new3={}
for key,val in a.items():
    new[key] = val


for key,val in b.items():
    if key not in new:
        new2[key] = val



for key,val in new2.items():
    if val >=3000:
        new3[key] = val
print(new3)