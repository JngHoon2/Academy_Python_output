
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

    print(dic1.get('id'))
    print(dic1.get('name'))
    print(dic1.get('department'))
    print(dic1.get('age'))
