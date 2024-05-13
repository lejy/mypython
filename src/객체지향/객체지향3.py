# name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진
# GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를
# 다음과 같이 문자열로 출력하는 코드를 작성하십시오.

class GraduateStudent:
    def __init__(self,major):
        self.major = major


class Student(GraduateStudent):
    def __init__(self,name,major=None):
        super().__init__(major)
        self.name = name
    def intro(self):
        if self.major is None:
            print("이름:",self.name)
        else:
            print("이름:",self.name,",전공:",self.major)


man = Student("홍길동")
man2 = Student("홍길동","컴퓨터")
man.intro()
man2.intro()