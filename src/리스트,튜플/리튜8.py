# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
a,b,c = 1,1,0
def pibo(x):
    if(x==1 or x == 2):
        return 1
    global a,b,c
    c = a+b
    a=b
    b=c


    return c


out = [pibo(i) for i in range(1,11)]

print(out)