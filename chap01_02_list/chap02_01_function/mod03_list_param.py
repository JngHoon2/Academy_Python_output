
## 파이썬 함수 집합구조 자료형(리스트, 딕셔너리 등) 인자 전달
# 함수 선언 부분(level 0)
# 리스트를 전달받는 함수
def fn_list_param(name_list):
    for n in name_list:
        print(n, end= ' ')

# 리스트를 반환하는 함수
def fn_return_list(num_list):
    list = []
    for n in num_list:
        list.append(n * 10)
    return list

# 딕셔너리를 전달하는 함수
def fn_dic_param(name_dic):
    for k in name_dic.keys():
        print('{0} : {1}'.format(k, name_dic.get(k)))

def main():
    # 리스트 전달
    name_list = ['홍길동', '010', '서울']
    fn_list_param(name_list)
    print()

    # 리스트를 반환 받음
    num_list = [10, 20, 30]
    num_list2 = fn_return_list(num_list)
    print(num_list2)

    dic1 = {'id':'20010301', 'name':'이미나', 'department':'컴퓨터공학과', 'age':23}
    fn_dic_param(dic1)

if __name__ == '__main__':
    main()