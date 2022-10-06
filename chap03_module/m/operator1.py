
# 덧셈 곱셈 함수 모듈로 m 패키지에 소속됨.

# 덧셈 함수
def addition(a, b):
    return a + b

# 뺄셈 함수
def subtraction(a, b):
    return a - b

#[level 0 실행 코드] 모듈 실행시 바로 실행됨.
sum = addition(3,4)
print('-------------------- 디버깅 --------------------')
print('addition(3,4) 결과 : {}'.format(sum))
sub = subtraction(8,3)
print('subtraction(8,3) 결과 : {}'.format(sub))