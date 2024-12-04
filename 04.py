import sys


source = sys.argv[1] if len(sys.argv) >= 2 else "04.txt"
d = open(source).readlines()

p1 = 0
p2 = 0
rows = len(d)
cols = len(d[0])

for r in range(rows):
    for c in range(cols):
        if d[r][c] == "X":
            # right
            if (
                c + 3 < cols
                and d[r][c + 1] == "M"
                and d[r][c + 2] == "A"
                and d[r][c + 3] == "S"
            ):
                p1 += 1
            # right down
            if (
                c + 3 < cols
                and r + 3 < rows
                and d[r + 1][c + 1] == "M"
                and d[r + 2][c + 2] == "A"
                and d[r + 3][c + 3] == "S"
            ):
                p1 += 1
            # down
            if (
                r + 3 < rows
                and d[r + 1][c] == "M"
                and d[r + 2][c] == "A"
                and d[r + 3][c] == "S"
            ):
                p1 += 1
            # left down
            if (
                r + 3 < rows
                and c - 3 >= 0
                and d[r + 1][c - 1] == "M"
                and d[r + 2][c - 2] == "A"
                and d[r + 3][c - 3] == "S"
            ):
                p1 += 1
            # left
            if (
                c - 3 >= 0
                and d[r][c - 1] == "M"
                and d[r][c - 2] == "A"
                and d[r][c - 3] == "S"
            ):
                p1 += 1
            # left up
            if (
                r - 3 >= 0
                and c - 3 >= 0
                and d[r - 1][c - 1] == "M"
                and d[r - 2][c - 2] == "A"
                and d[r - 3][c - 3] == "S"
            ):
                p1 += 1
            # up
            if (
                r - 3 >= 0
                and d[r - 1][c] == "M"
                and d[r - 2][c] == "A"
                and d[r - 3][c] == "S"
            ):
                p1 += 1
            # right up
            if (
                r - 3 >= 0
                and c + 3 < cols
                and d[r - 1][c + 1] == "M"
                and d[r - 2][c + 2] == "A"
                and d[r - 3][c + 3] == "S"
            ):
                p1 += 1

        if r + 2 < rows and c + 2 < cols and d[r + 1][c + 1] == "A":
            if (
                d[r][c] == "M"
                and d[r + 2][c + 2] == "S"
                and d[r][c + 2] == "M"
                and d[r + 2][c] == "S"
            ):
                p2 += 1
            if (
                d[r][c] == "M"
                and d[r + 2][c + 2] == "S"
                and d[r][c + 2] == "S"
                and d[r + 2][c] == "M"
            ):
                p2 += 1
            if (
                d[r][c] == "S"
                and d[r + 2][c + 2] == "M"
                and d[r][c + 2] == "M"
                and d[r + 2][c] == "S"
            ):
                p2 += 1
            if (
                d[r][c] == "S"
                and d[r + 2][c + 2] == "M"
                and d[r][c + 2] == "S"
                and d[r + 2][c] == "M"
            ):
                p2 += 1

print(p1)
print(p2)
