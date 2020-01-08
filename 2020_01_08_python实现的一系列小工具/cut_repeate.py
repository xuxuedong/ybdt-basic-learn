def lookupLines(f):
    lines = 0
    blankLines = 0
    for line in f.readlines():
        lines += 1
    print 'Lines are: ' + str(lines)

def lookupBlankLinesAndDelThem(f):
    blankLines = 0
    allLines = f.readlines()
    for line in allLines:
        i = 0
        if line == '\r\n' or line == '\n' or line == '\r':
            blankLines += 1
            del allLines[i]
        i += 1
    print 'Blank lines are: ' + str(blankLines)
    return allLines

def main():
    f = open('passwdFile.txt', 'r')
    func = raw_input('please input the index of the function that you want to execute: a(lookupLines) or b(lookupBlankLinesAndDelThem)? ')
    if func == 'a':
        lookupLines(f)
        f.close()
    else:
        allLines = lookupBlankLinesAndDelThem(f)
        f.close()
        f = open('passwdFile.txt', 'w')
        f.writelines(allLines)
        f.close()

if __name__ == "__main__":
    main()
