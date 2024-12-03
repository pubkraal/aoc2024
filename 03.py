import re

r = re.compile(r"(do|don't)\(\)|(mul\(([0-9]+),([0-9]+)\))")

tst = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

print(r.findall(tst))

with open("03.txt") as rd:
    d = rd.read().strip()
    instr = r.findall(d)
    p1 = 0
    p2 = 0
    active = True
    for m in instr:
        if m[1] != '':
            sm = int(m[2]) * int(m[3])
            p1 += sm
            if active:
                p2 += sm
        elif m[0] == 'do':
            active = True
        elif m[0] == "don't":
            active = False

    print("1:", p1)
    print("2:", p2)
