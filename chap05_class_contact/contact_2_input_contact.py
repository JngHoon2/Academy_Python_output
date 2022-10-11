
## 연락처 관리를 위한 기본 클래스 모듈 ##
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    print(name, phone_number, e_mail, addr)

# 모듈 자체 테스트 시, 호출할 함수
def run():
    set_contact()

# 모듈 자체 테스트인지, import 인지를 구분
if __name__ == '__main__':
    run()
