# 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.

man1 = input()
man2 = input()

win = {
    ("가위","보"):"Man1",
    ("바위","가위"):"Man1",
    ("보","바위"):"Man1",
    ("보","가위"):"Man2",
    ("가위","바위"):"Man2",
    ("바위","보"):"Man2"
}
Draw = {
    ("가위","가위"),
    ("바위","바위"),
    ("보","보")
}

if(man1,man2)in win:
    print("결과: %s Win!"% win[(man1,man2)])
elif(man1,man2) in Draw:
    print("결과: Draw")