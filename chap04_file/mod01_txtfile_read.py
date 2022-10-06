
## 파이썬 파일 입출력(읽기)
inFp = None
inStr = ""

filePath = "/Users/tuan/Documents/pythonWorks/chap04_file/text.txt"
# inFp = open(filePath, 'r', encoding='utf-8') # 파일 오픈, r = 읽기 전용

with open(filePath, 'r', encoding='utf-8') as inFp:
    # 없는 파일을 열경우 FileNotFoundError 발생

    # 한줄
    # inStr = inFp.readline()
    # print(inStr, end="")

    # 두줄
    # inStr = inFp.readline()
    # print(inStr, end="")

    # while True :
    #     inStr = inFp.readline()
    #     if inStr == "":
    #         break
    #     print(inStr, end="")

    # 리스트로 한꺼번에 읽기
    # readLines() : 파일 내용 전체를 가져와 리스트로 반환합니다.
    # 각 줄은 문자열 형태로 리스트(list)의 요소로 저장됩니다.
    inList = inFp.readlines() #<class 'list'>
    for inStr in inList:
        print(inStr, end="")