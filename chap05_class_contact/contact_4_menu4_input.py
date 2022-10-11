from contact_1_contact import Contact

# 사용자로부터 데이터 입력받기
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    print(name, phone_number, e_mail, addr)

    contact = Contact(name, phone_number, e_mail, addr)
    return contact
# ------- def set_contact()  END-----------

# 변경되는부분(추가)-------------------------------------

# 메인 메뉴 구성하기
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")

    return int(menu)
# ------ def print_menu(): END -------

# 모듈 자체 테스트 시, 호출할 함수
def run():
    # 객체 저장용 리스트
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)

        elif menu == 4:
            print("현재까지 만들어진 연락처 갯수 : ", len(contact_list))
            break

#모듈 자체 테스트 인지, import 인지를 구분
if __name__ == "__main__":
    run()