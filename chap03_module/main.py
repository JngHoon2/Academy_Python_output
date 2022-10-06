
# 모듈 자체를 임포트
import Module1

# 모듈 내부의 함수를 지정하여 임포트
from m.operator1 import addition, subtraction

def main():
    # Module1.func1()
    # Module1.func2()
    # Module1.func3()
    # print()

    print('[main모듈 디버깅] --------------------------------')
    hap = addition(2,3)
    subs = subtraction(6,3)
    print('main 모듈 덧셈 : {0} \nmain 모듈 뺄셈 : {1}'.format(hap, subs))

if __name__ == '__main__':
    main()
    