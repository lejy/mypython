# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

from random import randrange as rr
T = int(input())

cardLists = []
cardDict = {}

numCount = 0
countTool=()


for i in range(T):
    N = int(input())
    cardList = list(input())
    cardLists.append(cardList)

for j in range(len(cardLists)):
    countTool = cardLists[j]
    count = {}

    for card in countTool:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1

    maxCount = max(count.values())
    mostCards = [k for k,v in count.items() if v == maxCount]

    cardC = max(mostCards)
    cardDict[j] = (cardC,maxCount)


for i in cardDict:
    cardC,cardDict[i] = cardDict[i]
    print(f"#{i+1} {cardC} {cardDict[i]}")



