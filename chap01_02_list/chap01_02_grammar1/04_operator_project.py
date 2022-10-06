if __name__ == '__main__':
    money = int(input("금액을 입력하세요 : "))
    print("환전할 금액 %d원"%money)

    re1= int(money/10000)
    don=money%10000
    re2= int(don/5000)
    don=money%5000
    re3 = int(don/1000)
    don=money%1000
    re4 = int(don/ 500)

    print("10,000원권 %d장"%re1)
    print("5,000원권 %d장"%re2)
    print("1000원권 %d장"%re3)
    print("500원권 %d장" % re4)

