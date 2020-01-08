import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python.exe tmp.py path_to_dir")
        print("Example: python.exe tmp.py \"c:\\users\\xcblj\\desktop\\test\"")
        sys.exit(0)
    cwd = sys.argv[1]
    fd = os.listdir(cwd)
    
    '''
    def compare_it(x, y):
        x_index = x.find("-")
    y_index = y.find("-")
    
    # assume prefix only has 0-9 and 10-99
    if x_index == 1:
        x_ = x[0]
    else:
        x_ = x[0:2]
    if y_index == 1:
        y_ = y[0]
    else:
        y_ = y[0:2]
        
    if int(x_) > int(y_):
        return 1
    elif int(x_) < int(y_):
        return -1
    else:
        return 0
    '''
    
    # rename it
    for each in fd:
        if os.path.isfile(cwd + "\\" + each):
            if each[1] == "-":
                if each[0] >= "0" and each[0] <= "9":
                    os.rename( cwd + "\\" + each, cwd + "\\" + str(int(each[0]) + 1) + each.strip(each[0]) )
                else:
                    pass
            else:
                pass
        else:
            continue

if __name__ == "__main__":
    main()
