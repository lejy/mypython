# 다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,
# 이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.

a = input()

size = [int(x) for x in a if x != ',']

array = [[0 for x in range(size[1])] for _ in range(size[0])]

for i in range(size[0]):
    for j in range(size[1]):
        array[i][j] = i*j

print(array)
