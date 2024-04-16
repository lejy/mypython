# 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.

def battle():
    p1,p2,p1n,p2n='','','',''
    p1n = input()
    p2n = input()
    p1 = input()
    p2 = input()
    fight = (p1,p2)
    print(fight)
    win = [
        ("가위","보"),
        ("바위","가위"),
        ("보","바위")]
    draw = [
        ("가위","가위"),
        ("바위","바위"),
        ("보","보")
    ]
    if fight in win:
        print(f"{p1}이 이겼습니다!")
    elif fight in draw:
        print("무승부")
    else:
        print(f"{p2}가 이겼습니다!")


battle()