# 국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
# 메서드를 호출하는 코드를 작성해봅시다.

class Korean:
    def __init__(self):
        self.printNationality()
    @staticmethod
    def printNationality():
        print("대한민국")

kor = Korean()
print(kor.printNationality())