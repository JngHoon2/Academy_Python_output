
## 연락처 관리를 위한 기본 클래스 모듈 ##
class Contact:
    # 생성자(초기자)
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

#### class chap05_class_contact: END ####

def run():
    kim = Contact('김일구', '010-8812-1193', 'ilgu.kim@python.com', 'Seoul')
    lee = Contact('이일구', '010-8812-1193', 'ilgu.kim@python.com', 'Seoul')
    park = Contact('박일구', '010-8812-1193', 'ilgu.kim@python.com', 'Seoul')

    list = []

    list.append(kim)
    list.append(lee)
    list.append(park)

    print(list[0].name, list[0].phone_number, list[0].e_mail, list[0].addr)
    print(list[1].name, list[1].phone_number, list[1].e_mail, list[1].addr)
    print(list[2].name, list[2].phone_number, list[2].e_mail, list[2].addr)

    for i in list:
        print(i.name, i.phone_number, i.e_mail, i.addr)
    print()

    for i in range:
        print(list[i].name, list[i].phone_number, list[i].e_mail, list[i].addr)

if __name__ == '__main__':
    run()