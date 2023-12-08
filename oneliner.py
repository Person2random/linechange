def writealine(file,towrite,toline):
    toline -= 1
    lines = []
    with open(file,"r") as f:
        lines = f.readlines()
        lines[toline] = towrite + "\n"
    with open(file,"w") as f:
        for i in lines:
            f.write(i)

