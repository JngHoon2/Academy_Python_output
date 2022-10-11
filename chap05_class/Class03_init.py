
# Car 클래스 선언 부분
class Car:
    name = ""
    speed = 0

    # 생성자(초기화 값 전달)
    def __init__(self, name, speed):
        self.name = name    # self.name : 인스턴스 변수
        self.speed = speed

    # 차 이름 반환
    def get_name(self):
        return self.name

    # 속도
    def get_speed(self):
        return self.speed

# 전역 변수 선언 부분 #
car1, car2 = None, None

# 메인 코드 부분 #
car1 = Car("아우디", 0)    # 생성과 동시에 값 전달
car2 = Car("벤츠", 30)

print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (car1.name, car1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (car2.name, car2.speed))