
##추상 클래스(abstract Cass) 사용 클래스 ##
import Class06_abstract as abs

a = abs.Korea("대한민국", 50000000, '서울')

# 자식 클래스에 다음 코드 주석처리시 오류
# def show_capital(self):
#     super().show_capital()
#     print(self.capital)

a.show_name()
a.show_capital()
