if __name__ == '__main__':

    #리스트(list)
    #1.한번에 여러개의 값을 저장
    #2.리스트 변수 - [값1,값2,값3]
    #3.0부터 순차적으로 인덱스를 갖음
    #4.특정 인덱스 값을 변경 가능

    #[1] 리스트 선언 형태
    print('----리스트 선언 형태--------')
    list_num=[]
    list_num=[1,2,3,4,5]
    list_num2=[1,2,3,4.5,5.8,['파이썬','자바']]

    # print('list_num의 갯수 len()함수 : ',len(list_num))
    # print('list_num의 첫번째 값 : ',list_num[0])
    # print('list_num의 맨끝 값 : ',list_num[4])
    # print('list_num2의 맨끝값 : ',list_num2[len(list_num2)-1])
    # print(list_num[:5])
    # print(list_num[0:])

    #[2]리스트 반복
    print("------리스트 반복---------")
    print('1. list_num의 전체 요소 : ')
    for n in list_num:
        print(n,end="")
    print()

    print('3.모든 요소의 합은 : ')
    sum=0
    for n in list_num:
        sum+=n
    print(sum)
    print()

    print('3.짝수 요소의 합은 : ')
    sum = 0
    for n in list_num:
        if n%2==0:
            sum += n
    print(sum)
    print()

    print('3.삼항연산자_ 홀수 요소의 합은 : ')
    sum = 0
    for n in list_num:
        sum=sum+(n if n % 2 != 0 else 0)
    print(sum)
    print()

    #[3]리스트 조작함수
    print('-----리스트 함수-------')
    print('5.리스트에 숫자 6추가하기')
    list_num.append(6)
    print(list_num)

    #pop() 맨뒤 값 제거
    print('6.리스트 맨 뒤 값 제거하기 : ')
    list_num.pop()
    print(list_num)
    print()

    #remove(지울값)
    list_num.remove(1)
    print(list_num)

    #sort() 정렬
    print('7.리스트 정렬하기 : ')
    list_num.sort()
    print(list_num)

    #reverse()역순 정렬하기
    print('8. 리스트 역순 정렬하기')
    list_num.reverse()
    print(list_num)

    