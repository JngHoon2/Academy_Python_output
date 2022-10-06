
## 딕셔너리
# {key:value} 형태로 작성

if __name__ == '__main__':

    dic = {1:'홍길동', 2:'임꺾정', 3:'김두한', 4:'최두팔'}
    print(dic)
    print()

    dic1 = {'id': '20010301', 'name':'이미나', 'department':'컴퓨터공학과', 'age':23}
    dic1['phone'] = '010-1234-5678'
    print(dic1)
    print()

    print(dic1['id'])
    print(dic1['name'])
    print(dic1['department'])
    print(dic1['age'])
    print()

    # get 사용 시 키값이 없으면 값을 가져오지 않는다.(None 값을 가지고 오며, 오류가 발생하지 않는다.)
    print(dic1.get('id'))
    print(dic1.get('name'))
    print(dic1.get('department'))
    print(dic1.get('age'))
    print()


    singer = {'이름':'트와이스', '구성원수':9, '데뷔':'서바이벌 식스틴', '대표곡':'시그널'}
    # 딕셔너리.keys() 함수 : 딕셔너리의 모든 키를 반환
    for k in singer.keys():
        print('{0} : {1}'.format(k, singer.get(k)))
    print()

    # 딕셔너리.values() 함수 : 딕셔너리의 모든 값을 반환
    for value in list(dic.values()):
        print("{0}".format(value))
    print()

    # 딕셔너리.items() 함수 : 딕셔너리의 모든 (키, 값)을 반환
    for (key, value) in list(dic.items()):
        print(f'{key} --> {value}')
    print()

    # 최댓값 출력
    dic = {'홍길동':90, '김보람':80, '김정수':70}
    all_value = dic.values()
    max_value = max(all_value)
    print(max_value)

