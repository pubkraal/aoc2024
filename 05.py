from collections import defaultdict, deque
import sys

source = sys.argv[1] if len(sys.argv) >= 2 else "05.txt"
d = open(source).read()

rules, pages = d.split("\n\n", 1)
rules = rules.strip().split("\n")
pages = pages.strip().split("\n")

prb = defaultdict(set)
pra = defaultdict(set)

for r in rules:
    b, a = r.split("|")
    b, a = int(b), int(a)
    prb[b].add(a)
    pra[a].add(b)


def test_rules(pages):
    for i, x in enumerate(pages):
        for j, y in enumerate(pages):
            if i < j and y in pra[x]:
                return False

    return True


p1 = 0
p2 = 0

for page in pages:
    nms = [int(x) for x in page.split(",")]
    if test_rules(nms):
        p1 += nms[len(nms) // 2]
    else:
        fixed = []
        queue = deque([])
        todo = {n: len(pra[n] & set(nms)) for n in nms}
        for n in nms:
            if todo[n] == 0:
                queue.append(n)
        while queue:
            x = queue.popleft()
            fixed.append(x)
            for y in prb[x]:
                if y in todo:
                    todo[y] -= 1
                    if todo[y] == 0:
                        queue.append(y)
        p2 += fixed[len(fixed) // 2]

print(p1)
print(p2)
