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

# 연락처 리스트 출력
def print_contact_list(contact_list):
    if(len(contact_list) == 0):
        print("사용자가 존재하지 않습니다.")

    for contact in contact_list:
        contact.print_info()

# 연락처 정보 삭제
def delete_contact(contact_list, name):
    if len(contact_list) == 0:
        print("사용자가 존재하지 않습니다.")

    for index, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[index]

# 파일로 연락처 저장
def save_contact(contact_list):
    file = open("contact_db.txt", mode="wt", encoding="utf-8")
    for contact in contact_list:
        file.write(contact.name + '\n')
        file.write(contact.phone_number + '\n')
        file.write(contact.e_mail + '\n')
        file.write(contact.addr + '\n')
    file.close()

def load_contact(contact_list):
    file = open("contact_db.txt", mode="rt", encoding="utf-8")
    lines = file.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4 * i].rstrip("\n")
        phone_number = lines[4 * i + 1].rstrip("\n")
        e_mail = lines[4 * i + 2].rstrip("\n")
        addr = lines[4 * i + 3].rstrip("\n")

        contact = Contact(name, phone_number, e_mail, addr)
        contact_list.append(contact)
    file.close()

# 메인 메뉴 구성하기
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")

    return menu
# ------ def print_menu(): END -------

# 모듈 자체 테스트 시, 호출할 함수
def run():
    # 객체 저장용 리스트
    contact_list = []

    load_contact(contact_list)

    while 1:
        menu = print_menu()

        if not menu.isdigit():
            print("정수만 입력하세요.")
            continue

        menu = int(menu)

        if(menu < 1) | (menu > 4):
            print("=============> [1 - 4 사이의 숫자를 입력하세요.]")
            continue

        if menu == 4:
            save_contact(contact_list)
            break

        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
            print("현재까지 입력된 연락처는 : {0}명입니다.".format(len(contact_list)))
        elif menu == 2:
            print_contact_list(contact_list)
        elif menu == 3:
            name = input("삭제할 연락처 이름을 입력하세요.")
            delete_contact(contact_list, name)



#모듈 자체 테스트 인지, import 인지를 구분
if __name__ == "__main__":
    run()