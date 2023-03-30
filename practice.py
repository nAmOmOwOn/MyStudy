inFile = None
inStr = ""

inFile = open("C:/myData1.txt", "r", encoding="UTF-8")

num = 0
while True:
    inStr = inFile.readline()
    num += 1
    if inStr == "":
        break
    print(str(num),":",inStr, end = '')

inFile.close()