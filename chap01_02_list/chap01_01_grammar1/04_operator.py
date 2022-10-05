if __name__ == '__main__':

    # #1.산술 연산자
    # print('------------산술 연산자-------------')
    # print(1+1)
    # print(2*3)
    # print(6/2)
    # print(9/4)
    # print(9//4)
    # print(2 **3)
    # print(5%3)
    #
    # #2. 파이썬에는 증감연산자가 없다.
    # print('------------------------증강연산자 없음--------------------')
    #
    # num =70
    # num += 1
    # print(num)
    # #print(num +=1)
    #
    # #3.관계 연산자 - 같은지, 큰지, 작은지 비교 결과는 True/False
    # print('-------------------관계 연산자-------------')
    # print(2>3)
    # print(5 <=5)
    # print(2!=3)
    # print(not 2==3)
    # print(not 2 !=3)

    # # 4. 논리 연산자 -not,and,or 여러가지 조건을 연결해주는 역할
    # print('--------논리 연산잔--------')
    # print((2 < 3) and (4 < 5))
    # print((2 < 3) & (4 < 5))
    # print((2 == 3) or (4 < 5))
    # print(not ((2 == 3) | (4 < 5)))
    #
    # # 5.멤버 연산자(in,not in) 특정 값이 ㅇ있는지 없는 지 확인
    # print('---------멤버 연산자 ---------')
    # str_fruit = ['딸기', '포도', '사과', '배']
    # if '딸기' not in str_fruit:
    #     print('딸기는 과일 목록에 없어요')
    # else:
    #     print('딸기는 과일 목록에 있어요')
    #
    # # 6.식별연산자 - 특정 객체의 주솟값 확인
    # print('------------식별 연산자------------')
    # print('str_fruit 객체의 번짓수는 : ', id(str_fruit))

    #7.연산자 우선순위
    # 1순위 - 괄호, 리스트 , 튜플, 딕셔너리, 세트
    # 다음순위 -산술 > 관계 > 논리연산자 순서
    # print(2*3+5)
    # print(2*(3+5))
    # print((2<3)and(4<5))
    #
    # #8.그외 유용한 함수
    # print(max(1,2,3))
    # print(min(1,2,3))
    #
    # # 9 math 함수
    # import math
    #
    # pi = 3.141592
    # print('math.ceil(pi):', math.ceil(pi))  # ceil 무조건 올림
    # print('math.floor(pi):', math.floor(pi))  # floor 무조건 내림
    #
    # #10. 삼항 연산자
    # result= int(input("점수를 입력하시오"))
    # result = "합격" if result >=60 else "불합격"
    # print(result)

    #11.삼항연산자를 통한 윤년 출력하기
    #윤년공식 = (년도%400) or ((년도 %4==0) and (년도 %100!=0))

    # year= int(input("년도를 입력하세요. : "))
    # isLeapYear = year %400==0 or (year %4 ==0 and year%100 !=0)
    # str_leaf = "윤년" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "평년"
    # # print(isLeapYear)
    # print("%d년은 %s입니다." %(year, '윤년' if isLeapYear else '평년'))
    # print("%d년은 %s입니다." % (year, '홀수' if year%2 else '짝수'))
    # print(str_leaf)

    #12.변환함수(숫자로 구성된 문자열을 int, float로 변환)
    float1="99.123"
    b1=float(float1)
    print(b1)
    print()

    int1='99'
    b2=int(int1)
    print(b2)
    print()

    str_val=b1+b2
    print((type(str_val)))
    print(str_val)

    str_val=str(b1)+str(b2)
    print(type(str_val))
    print(str_val)