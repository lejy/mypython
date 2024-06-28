'''
1. maxMachine 클래스를 완성하세요.
2. sorting 함수를 완성하세요.
'''

class maxMachine :
    '''
    이곳에 '최댓값 기계' 문제에서 작성했던 클래스를 붙여넣으세요
    '''
    def __init__(self) :
        self.myData = []

    def addNumber(self, n) :
        self.myData.append(n)

    def removeNumber(self, n) :
        self.myData.remove(n)

    def getMax(self) :
        return max(self.myData)

def sorting(myList) :
    '''
    myList를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.

    예를 들어, myList = [5, 2, 3, 1] 이라면 [5, 3, 2, 1] 을 반환해야 합니다.

    단, maxMachine class를 이용하도록 합니다.
    '''

    myMachine = maxMachine()

    result = []

    for element in myList:
        myMachine.addNumber(element)

    for i in range(len(myList)) :
        myMax = myMachine.getMax()
        result.append(myMax)
        myMachine.removeNumber(myMax)


    return result