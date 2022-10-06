
## 파이썬 파일 입력 오류 처리(읽기 오류)

import os

inFp = None
inStr = ""
fName = ""
inList = []
inStr = ""

filePath = "/Users/tuan/Documents/pythonWorks/chap04_file/text.txt"

if os.path.exists(filePath):
    with open(filePath, 'r', encoding='utf-8') as inFp: #with ~ as 파일 닫기 자동처리

        inList = inFp.readlines()

        for inStr in inList:
            print(inStr, end="")
else :
    print("%s 해당 경로에 해당 파일이 존재하지 않습니다." % filePath)