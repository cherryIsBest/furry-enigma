txt1 = open(r"D:\code\fileOne.txt")
txt2 = open(r"D:\code\fileTwo.txt")
txt1Out = txt1.readlines()
txt2Out = txt2.readlines()
print("number of lines on fileOne.txt =", len(txt1Out))
print("number of lines on fileTwo.txt =", len(txt2Out))
for txt1Line in txt1Out:
    print("Word per line =", txt1Line)
    for txt2Line in txt2Out:
        print("Word per line =", txt2Line)
        if txt1Line == txt2Line:
            print("Ok","\n","-|*|-"*20,"\n")
        elif txt1Line != txt2Line:
            print("Not good","\n","-|*|-"*20,"\n")
txt1.close()
txt2.close()
