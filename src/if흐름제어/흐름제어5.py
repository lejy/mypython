# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 출력 시 아스키코드를 함께 출력합니다.

a = input()
asci = ord(a)
if(asci>=97 and asci<=122):
    out = asci - 32
    al = chr(out)
    print("%c(ASCII:%d) => %c(ASCII: %d)"%(a,asci,al,out))
elif(asci>=65 and asci<=90):
    out = asci + 32
    al = chr(out)
    print("%c(ASCII:%d) => %c(ASCII: %d)"%(a,asci,al,out))

else:
    print(a)