
class Flight:

    # 생성자에서 객체의 Validation 진행
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("첫 두글자가 알파벳이 아닙니다.")   # 의도적인 예외 발생
        if not number[:2].isupper():
            raise ValueError("첫 두글자가 대문자가 아닙니다.")
        if not number[2:].isdigit():
            raise ValueError("세번째 글자 이상이 양의 숫자가 야닙니다.")
        self._number = number   # 이 시전에서 맴버변수가 만들어짐(Flight class의 전역변수)

    # 비행기 넘버 조회
    def get_number(self):   # 클래스의 모든 메소드의 파라미터는 self를 전달해야함
        return self._number

def main():
    f = Flight('AB2548')
    print(f.get_number())

if __name__=='__main__':
    main()