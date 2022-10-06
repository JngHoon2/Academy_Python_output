
## 파이썬 함수(function)

# 함수 선언 부분(level 0)

# 여러 개의 인자를 전달 맏는 함수
def fn_contact(name, phone, email, addr):
    print("이름 : {}".format(name))
    print("연락처 : {}".format(phone))
    print("이메일 : {}".format(email))
    print("주소 : {}".format(addr))

    return name + '\t' + phone + '\t' + email + '\t' + addr

def fn_multi_return(id, pw):
    print('전달받은 아이디{}'.format(id))
    print('전달받은 비밀번호{}'.format(pw))
    return id, pw

def main():
    str = fn_contact('홍길동', '010-1234-5678', 'a@a.com', '서울특별시')
    print(f'여기는 main함수, 돌려받은 반환값은{str}')
    print()

    (id, pwd) = fn_multi_return('python', '1234')
    print('돌려받은 id {0} / pw {1}'.format(id, pwd))

if __name__ == '__main__':
    main()