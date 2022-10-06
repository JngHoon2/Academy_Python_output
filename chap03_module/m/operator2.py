
# 곱셈 나눗셈 함수 모듈로 m 패키지에 소속됨.

# 곱셈 함수
def multiplication(a, b):
    return a * b

# 나눗셈 함수
def division(a, b):
    return int(a / b)

#[level 0 실행 코드] 모듈 실행시 바로 실행됨.
mul = multiplication(3,4)
print('-------------------- 디버깅 --------------------')
print('multiplication(3,4) 결과 : {}'.format(mul))
div = division(6,3)
print('division(6,3) 결과 : {}'.format(div))