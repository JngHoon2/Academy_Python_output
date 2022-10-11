
class Product:
    # 생성자
    def __init__(self, pdInfo):
        self.pdCode = pdInfo[0]
        self.pdName = pdInfo[1]
        self.pdPrice = int(pdInfo[2])
        self.pdLeftCount = int(pdInfo[3])
        self.pdSellCount = int(pdInfo[4])
    # 판매금액
    def sellTotalMoney(self):
        return self.pdSellCount * self.pdPrice
    # 남은금액
    def leftTotalMoney(self):
        return self.pdLeftCount * self.pdPrice

class Main:
    def __init__(self):
        self.pdDict = {}

    def working(self):
        filePath = 'C:/filetest/test.txt'
        productFile = open(filePath, 'rt')  # rt : read and text로 r과 동일
        fileLines = productFile.readlines() # 내용을 한번에 모두 읽어옴(변환형 리스트)
        print(fileLines)

        for line in fileLines:
            line = line.replace('\n', '')
            lineInfo = line.split('\t')
            product = Product(lineInfo)
            self.pdDict[lineInfo[0]] = product

        print('===========================================================')
        print(' 상품코드    상품명     가격      남은수량    판매수량    ')
        print('===========================================================')
        for key, value in self.pdDict.items():
            print("pdCode : {} pdname : {} pdPrice : {} pdLeftCount : {} pdSellCount : {}"
                  .format(self.pdDict[key].pdCode, self.pdDict[key].pdName, self.pdDict[key].pdPrice,
                          self.pdDict[key].pdLeftCount, self.pdDict[key].pdSellCount))
        print('===========================================================')

# class end #

if __name__ == '__main__':
    main = Main()
    main.working()