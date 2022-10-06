
# 파이썬 binary 파일 복사
# binary 파일은 인코딩 불필요!

inFp, outFp = None, None
inStr = ""
inputFilePath = "/Users/tuan/Documents/pythonWorks/chap04_file/img.jpeg"
outputFilePath = "/Users/tuan/Documents/pythonWorks/chap04_file/img2.jpeg"

inFp = open(inputFilePath, 'rb')    # 읽기모드 : r -> rb로 (read binary mode)
outFp = open(outputFilePath, 'wb')  # write binary mode

while True:
    inStr = inFp.read(1)
    if not inStr:
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print("이진 파일 복사 완료!")