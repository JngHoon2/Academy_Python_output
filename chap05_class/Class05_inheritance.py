
## 클래스 상속 ##
# 부모 클래스
class Car:
    def method(self):
        print("슈퍼 클래스", end=' ')

# 자손 클래스
class Sedan(Car):  # 인자로 부모 클래스 전당 받겠다고 선언하면 파이썬이 상속해줌
    def method(self):
        print("서브 클래스 ", end=' ')

myCar = Car()   # 부모 객체 생성
myCar.method()  # 부모 객체 메소드 호출
print()

mySedan = Sedan()   # 자손 객체 생성
mySedan.method()    # 자식 객체 메소드 호출

