
### 파이썬 함수(function)

# 함수 선언 부분(level 0, 레벨 0)
# [1] 인자가 없고 리턴 값이 없는 함수
def fn_no_param():
    print('인자가 없는 함수 fn_no_param() 입니다.')

# [2] 인자가 있고 리턴 값이 없는 함수
def fn_param(fn_param1):
    print('fn_param() 함수에 인자로 전달된 값은 {0}입니다.'.format(fn_param1))

# [3] 인자다 있고 리턴 값도 있는 하무
def fn_param_return(str):
    print('fn_param_return() 함수에 전달된 인자는 {0}입니다.'.format(str))
    return str

def main():
    fn_no_param()
    fn_param("홍길동")
    c = fn_param_return("클라우드")
    print('여기는 main()함수, 돌려 받은 반환 값은 : {0}'.format(c))

if __name__ == '__main__':
    main()