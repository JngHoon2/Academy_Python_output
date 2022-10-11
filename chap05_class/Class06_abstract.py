
##추상 클래스(abstract Cass)란 ##
# 추상 클래스란 내용이 없는 미구현 메소그(추상메소드)를 한개 이상 가진 클래스이다.
# 자손 클래스에서 해당 추상 메소드를 구현하도록 강제함!!
# 상속받은 클래스는 해당 추상메소드를 구형하지 않아도, import할 때까지 에러는 발생하지 않으나
# 객체를 생성할때 에러 발생
# 추상 클래스르 사용할 때는 파이썬 기본 라이브러리 중 하나인 abc를 사용함.(abc 모듈을 import)
# 추상 클래스 내에 추상 메소드가 필요하다면 해당 메서드 위에 @abstractmethod 데코에리터를 추가
# 추상 메소드를 생략하면 기본적인 클래스 기능은 동작, 하지만 추상메소드룰 추가한 후에는 객체를 생성한 후에는 객체를 생성하면 에러발생

from abc import *   # 추상 메소드 사용시 abc 모듈을 import 해야함.

from abc import ABCMeta

# (metaclass=ABCMeta)
# metaclass는 클래스를 제어하는 클래스로, 여ㅑ기서는 AbstractCountry 클래스를
# ABCMeta 클래스로 제어하기 위해서 사용함
class AbsrtactCountry(metaclass=ABCMeta):
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show_capital(self):
        print('국가 클래스의 메소드입니다.')

        @abstractmethod
        def show_capital(self):
            print('국가의 수도는')

class Korea(AbsrtactCountry):

    # 생성자
    def __init__(self, name, population, capital):
        self.name = name    # 전역변수(멤버변수)
        self.polulation = population
        self.capital = capital

    def show_name(self):
        print('국가 이름은 : ', self.name)

    def show_capital(self):
        super().show_capital()
        print(self.capital)