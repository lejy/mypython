# 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.



def fib(x):
    result =[]
    a, b = 0, 1
    result.append(b)
    for i in range(0,x-1):
        c = a+b
        a,b = b,c
        result.append(c)
    print(result)



fib(int(input()))
