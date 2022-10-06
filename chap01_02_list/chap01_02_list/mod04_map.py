
#map
# 리스트의 변형, 리스트를 원하는 형태로 바꾸기 map() 함수

def ten_times(x):
    return x * 10

def bigger_five(x):
    return x >= 5

if __name__ == '__main__':
    # 사용형태
    # map(함수명(인자없이), (리스트, 튜플))
    # 반환값
    # map() 함수의 반환 값은 iterable(map object) 객체이기 때문에 다시 리스트로 반환
    # 동작 매커니즘
    # 첫 번쨰 인자인 함수에 두번쨰 인자인 집합 자료형의 값을 하나씩 넣어서 함수를 실행한다.
    # 그 결과가 iterable 객체에 담겨서 반환된다.

    # [1] 일반 함수를 사용한 리스트 형변환
    # 별도의 함수를 정의하여 다음 리스트의 모든 수에 10을 곱해서 새로운 리스트 생성
    list_num = [1,2,3,4,5,6,7,8,9,10]
    list_num2 = []

    # map()함수의 실행 결과가 iterable이기 때문에 list()함수를 사용하여 list로 현변환
    list_num2 = list(map(ten_times, list_num))

    # 리스트에서 하나싹 값을 꺼내서 출력
    for i in list_num2:
        print(i, end=' ')
    print()

    # 문자열(float) 리스트 float 타입으로 변환
    originalList = ['2.0', '4.0', '6.0', '8.0', '10.0', '12.0'] #문자열 리스트
    floatList = list(map(float, originalList)) # 문자열 리스트를 float 타입 리스트로 변환
    print(floatList)
    print()

    # 문자열(int) 리스트 int 타입으로 변환
    originalList = ['2', '4', '6', '8', '10', '12']  # 문자열 리스트
    intList = list(map(int, originalList))  # 문자열 리스트를 int 타입 리스트로 변환
    print(intList)
    print()

    #[필터링] filter
    newList = list(filter(bigger_five, list_num))
    print(newList)
    print()

    #[필터링] 람다함수 사용
    newList = list(filter(lambda x : x >= 5, list_num))
    print(newList)
    print()

    # [2] 람다함수를 사용한 리스트 형변환
    # 람다 함수를 이용하여 다음 리스트의 모든 수에 10을 곱해서 새로운 리스트를 만들 수 있다.
    list_num_lambda = list(map(lambda  x: x * 10, list_num))
    print(list_num_lambda)
    print()

    # 람다 함수를 이용하여 두 개의 인자를 받는 경우
    list_num_lambda = list(map(lambda x, y, z : x * y * z, [2,3,4], [1,2,3], [2,3,4]))
    print(list_num_lambda)
    print()

