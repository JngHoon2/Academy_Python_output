
#### 연산자[operator]

if __name__ == '__main__':
    print(1 + 1)
    print(2 * 3)
    print(6 / 2)
    print(9 / 4)
    print(9 // 4)
    print(2 ** 3)
    print(5 % 3)

    # 파이썬은 증감연산자가 없음.
    num = 70
    num += 1

    print(num)
    # print(num += 1)

    # 관계 연산자
    print(2 > 3)
    print(5 <= 5)
    print(2 != 3)
    print(not 2 == 3)
    print(not 2 != 3)

    print((2 > 3) and (4 < 5))
    print((2 < 3) & (4 < 5))
    print((2 == 3) or (4 < 5))
    print((2 == 3) | (4 < 5))
    print(not((2 == 3) | (4 < 5)))

    # 멤버 연산자
    str_fruit = ['딸기', '포도', '사과', '배']
    if '딸기' not in str_fruit:
        print("딸기가 과일 목록에 없습니다.")
    else :
        print("딸기가 과일 목록에 존재합니다.")

    # 식별 연산자 - 특정 개체의 주솟값 확인
    print('str_fruit 객체의 메모리주소는 : ', id(str_fruit))

    # 연산자 우선순위
    # 1순위 - 괄호, 리스트, 튜플, 딕셔너리, 세트
    # 다음 순위 - 산술 > 관계 > 논리 연산자
    print(2 * 3 + 5)
    print(2 *(3 + 5))
    print((2 < 3) and (4 < 5))

    print(max(1,2,3))
    print(min(1,2,3))

    import math
    pi = 3.141592
    print('math.ceil(pi) : ', math.ceil(pi))
    print('math.floor(pi) : ', math.floor(pi))

    # 삼항연산자
    result = int(input("점수를 입력하세요."))
    result = "합격" if result >= 60 else "불합격"
    print(result)

    year = int(input("년도를 입력하세요."))
    isLeapYear = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    print(isLeapYear)
    print("%d년은 %s입니다." % (year, '윤년' if isLeapYear else '평년'))
    print("%d년은 %s입니다." % (year, '홀수' if year else '짝수'))

    str_leaf = '윤년' if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else '평년'
    print(str_leaf)

    float1 = "99.123"
    b1 = float(float1)
    print(b1)

    int1 = "99"
    b2 = int(int1)
    print(b2)

    str_val = b1 + b2
    print(str_val)

    str_val = str(b1) + str(b2)
    print(type(str_val))
    print(str_val)