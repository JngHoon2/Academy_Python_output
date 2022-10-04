

## 환전 자판기
# 1. 조건 다음의 화폐 단위로만 환전할 수 있다.
# - 10000원, 5000원, 1000원, 500원
# 2. 금액을 입력받아서 위의 화폐 단위로 환전하는 알고리즘을 만드세여.

if __name__ == '__main__':
    don = input("환전할 금액을 입력하세요.")
    print(f"환전할 금액 {don}원")

    don = int(don)

    a = don // 10000
    don = don - a * 10000
    print(f"10000원권 {a}장")

    b = don // 5000
    don = don - b * 5000
    print(f"5000원권 {b}장")

    c = don // 1000
    don = don - c * 1000
    print(f"1000원권 {c}장")

    d = don // 500
    don = don - d * 500
    print(f"500원 동전 {d}개")

    print(f"짤짤이 : {don}원")