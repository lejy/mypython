

class ListPipe:

    def __init__(self) :


        self.myPipe = []


    def addLeft(self, n) :

        self.myPipe.insert(0,n)

    def addRight(self, n) :

        self.myPipe.append(n)

    def getBeads(self) :

        return self.myPipe


def processBeads(myInput) :
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''

    myPipe = ListPipe()

    for a, b in myInput:
        if b == 0:
            myPipe.addLeft(a)
        elif b == 1:
            myPipe.addRight(a)

    result = myPipe.getBeads()

    return result