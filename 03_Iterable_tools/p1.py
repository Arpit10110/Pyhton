try:
    f=open("./data.txt")
    # print(f.readline()) using this we can read the single line at once

    for line in f:
        print(line,end="")
    
    f2=open("./data.txt",'a')
    f2.writelines("\nSahi hai bhai")
    f2.close()
    f1 = open("./data.txt",'r')
    print("\n------------------")
    while True:
        lines = f1.readline()
        if lines=="":
            break
        print(lines,end="")
except NameError:
    print(NameError)