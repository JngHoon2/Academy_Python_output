
## 파이썬 함수 가변 파라미터

# 가변 파라미터 : 인자 값이 몇개가 올지 모름 (인자 앞에 *표)
# 전달 형태는 튜플
# 딕셔너리 형태로 넘기고 싶으면 *를 두개 붙이면 됩니당.

def avg(x, *more):
    return float(x + sum(more)) / (1 + len(more))

def main():

    hap = avg(10)
    print(f'매개변수가 1개인 함수를 호출한 결과 ===> {hap}')

    hap = avg(10, 20)
    print(f'매개변수가 2개인 함수를 호출한 결과 ===> {hap}')

    hap = avg(10, 20, 30)
    print(f'매개변수가 3개인 함수를 호출한 결과 ===> {hap}')

if __name__ == '__main__':
    main()