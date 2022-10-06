
# 파이썬 텍스트 파일 복사

inFp, outFp = None, None
inStr = ""
filePath = "/Users/tuan/Documents/pythonWorks/chap04_file/copy.txt"
inFp = open("/Users/tuan/Documents/pythonWorks/chap04_file/memo.txt", 'r', encoding='utf-8')
outFp = open(filePath, 'w')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("파일복사 완료!")
