
# 전역변수(global) / 지역변수(local) 네임스페이스

a = 20

def func1():
    a = 10
    print('func1()에서의 a값 : %d' % a)

def func2():
    print('func2()에서의 a값 : %d' % a)

def func3():
    global a
    a = 30

def main():
    func1()
    func2()
    print('main함수-1 a : ', a)
    func3()
    print('main함수 a : ', a)

if __name__ == '__main__':
    main()