
class Smartphone:

    def __init__(self, brand, information):
        # pring(type(brand), type(information))
        self.brand = brand
        self.information = information
        self.test_dict = {'a' : 1, 'b' : 2}
        self.test_list = {'1', '2', '3'}

    def __str__(self):
        return f'str : {self.brand} - {self.information}'

    def __repr__(self):
        return f'repr : {self.brand} - {self.information}'

Smartphone1 = Smartphone('Iphone', {'color':'White', 'price':10000})
Smartphone2 = Smartphone('Galaxy', {'color':'Black', 'price':8000})

# __dict__ : 객체를 문자열로 반환
# 클래스 댇테의 속성 정보를 확인하기 위해 사용
# 객체가 가진 여러가지 속성들을 딕셔너리 형태로 편하게 확인할 수 있다.
print('Smartphone1.__dict__: ', Smartphone1.__dict__)
# __str__
# 자바의 toString()과 같은 역활
print('Smartphone2.__str__ :', Smartphone2.__str__())