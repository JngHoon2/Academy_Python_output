
class Student:
    # 생성자
    # def __init__(self, name, kor, eng, math):
    #     self.name = name
    #     self.kor = kor
    #     self.eng = eng
    #     self.math = math

    # def __init__(self, sdInfo):
    #     self.sdNum = int(sdInfo[0])
    #     self.sdName = sdInfo[1]
    #     self.kor = int(sdInfo[2])
    #     self.eng = int(sdInfo[3])
    #     self.math = int(sdInfo[4])

    def __init__(self, sdInfo):
        self.sdName = sdInfo[0]
        self.kor = int(sdInfo[1])
        self.eng = int(sdInfo[2])
        self.math = int(sdInfo[3])

    # 총점
    def sum(self):
        sum = self.kor + self.eng + self.math
        return sum
    # 평균성적
    def avg(self):
        avg = round(self.sum() / 3, 2)
        return avg

# students = []
# students.append(Student('임꺽정', 77, 91, 70))
# students.append(Student('홍길동', 87, 58, 76))
# students.append(Student('이미온', 80, 65, 84))
# students.append(Student('정철희', 68, 38, 28))
# students.append(Student('사호정', 75, 85, 64))
# students.append(Student('은성준', 55, 66, 91))
#
# print('===========================================================')
# print(' 순번    이름     국어     영어    수학   총점  평균')
# print('===========================================================')
# i = 1
# for s in students:
#     print("{}    {}  {}  {}  {}  {}  {}".format(i, s.name, s.kor, s.eng, s.math, s.sum(), s.avg()))
#     i+=1
# print('===========================================================')

class Main:
    def __init__(self):
        self.sdDict = {}


    def working(self):
        filePath = 'C:/filetest/txt/score.txt'
        studentFile = open(filePath, 'rt', encoding='utf-8')      # rt : read and text로 r과 동일
        fileLines = studentFile.readlines()     # 내용을 한번에 모두 읽어옴(변환형 리스트)
        print(fileLines)

        for line in fileLines:
            line = line.replace('\n', '')
            lineInfo = line.split('\t')
            student = Student(lineInfo)
            self.sdDict[lineInfo[0]] = student

        print('===========================================================')
        print(' 순번    이름     국어     영어    수학   총점     평균')
        print('===========================================================')

        i = 1
        for key, value in self.sdDict.items():
            print(" {}\t  {}\t {}\t\t{}\t\t{}\t  {}\t {}"
                  .format(i, self.sdDict[key].sdName,  self.sdDict[key].kor,
                          self.sdDict[key].eng, self.sdDict[key].math, self.sdDict[key].sum(), self.sdDict[key].avg()))
            i+=1
        print('===========================================================')


# class end #

if __name__ == '__main__':
    main = Main()
    main.working()