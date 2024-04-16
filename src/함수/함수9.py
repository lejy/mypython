# 인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고
# 결과를 출력하는 프로그램을 작성하십시오.

a = input()
def longer(*a):
    if len(a[0])>len(a[1]):
        print(a[0])
    else:
        print(a[1])



hello = [x for x in a.split(",")]
longer(*hello)
