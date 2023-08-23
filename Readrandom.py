import random
def ReadRandom(limit,fname):
    f = open(fname,encoding="utf8")
    lines = f.readlines()
    lines = [i.strip() for i in lines]
    length = len(lines)
    count,string = 0,""
    while count < limit:
        r1 = random.randint(0,length - 1)
        string += " " + lines[r1]
        count += 1
    f.close()
    return string

