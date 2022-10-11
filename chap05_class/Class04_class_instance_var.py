
## 인스턴스 변수, 클래슽 변수 ##
# 1. 인스턴스 변수 : 객체(인스턴스)를 생성해야 사용할 수 있는 변수로 인스턴스 내에 공간 할당
#   - self.속성(변수) 형태로 할당했던 변수들은 모두 인스턴스 변수(속성)
# 2. 클래스 변수 : 클래스 안에 공간이 할당되어 여러 인스턴스가 공유
#   - 인스턴스 내에 공간이 별도로 마련되지 않음

class Car:
    color = ""  # 인스턴스 변수
    speed = 0   # 인스턴스 변수
    count = 0   # 클래스 변수로 사용 예정(변수 선언 시점에는 인스턴스/클래스 변수 구분 안둠)

    def print_massage(self):
        print("시험 출력합니다.")

    # 생성자
    def __init__(self):
        self.speed = 0  # self를 붙여서 인스턴스 변수
        Car.count += 1  # 클래스명.count로 접근했으므로 클래스 변수가 됨.

def main():
    # 변수선언
    myCar1, myCar2 = None, None

    # 메인 코드 부분
    myCar1 = Car()
    myCar1.speed = 30
    print("생산된 자동차는 총 %d대 입니다." % (Car.count))

    myCar2 = Car()
    myCar2.speed = 60
    # myCar2.count응 통해서도 클래스 변수에 접근 가능.
    print("생산된 자동차는 총 %d대 입니다." % (myCar2.count))

if __name__=='__main__':
    main()