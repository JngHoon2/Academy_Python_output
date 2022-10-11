
## 클래스 상속2 ##
# 국가 클래스(부모)
class Country:
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')

# 자손 클래스
class Korea(Country):  # Countrty 클래스 상속

    # 생성자
    def __init__(self, name):
        print('Korea 클래스 name : ', name)
        self.name = name    # 전역변수(멤버변수)

    # 국가명 조회 메소드
    def show_name(self):
        print('국가 이름은 : ', self.name)
        return self.name

    # 오버라이딩
    def show(self):
        print('자식이 오버라이딩한 메소드입니다. 국가는', self.show_name())

def main():
    a = Korea('대한민국')
    a.show()    # 상속 받았기 때문에 show() 메소드가 들어와 있음, 하지만 부노의 show() 호출됨
    # a.show_name()   # 자식이 확장한 메소드
    # print(a.name)
    # print(a.capital)

if __name__ == '__main__':
    main()