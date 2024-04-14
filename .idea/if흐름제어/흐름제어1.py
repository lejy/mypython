# 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오

a = int(input())

if a == 1:
    print("1의 약수: 1")
elif a == 2:
    print("2의 약수: 1, 2")
elif a == 3:
    print("3의 약수: 1, 3")
elif a == 4:
    print("4의 약수: 1, 2, 4")
elif a == 5:
    print("5의 약수: 1, 5")
elif a == 6:
    print("6의 약수: 1, 2, 3, 6")
elif a == 7:
    print("7의 약수: 1, 7")
elif a == 8:
    print("8의 약수: 1, 2, 4, 8")
elif a == 9:
    print("9의 약수: 1, 3, 9")
else:
    print("10 이상의 수는 처리할 수 없습니다.")
