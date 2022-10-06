
## 파이썬 파일 출력(쓰기)

outFp = None
outStr = ""
filePath = "/Users/tuan/Documents/pythonWorks/chap04_file/memo.txt"

outFp = open(filePath, 'w')

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("파일 출력 종료!")