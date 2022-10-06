
## 파이썬 함수(function) default

def fn_default_param(v1, v2, v3 = 0):
    result = 0
    result = v1 + v2 + v3
    return result

def main():
    hap = fn_default_param(10, 20)
    print(f'매개변수가 2개인 함수를 호출한 결과 ===> {hap}')

    hap = fn_default_param(10, 20, 30)
    print(f'매개변수가 3개인 함수를 호출한 결과 ===> {hap}')

if __name__ == '__main__':
    main()