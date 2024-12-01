from collections import Counter

lines = open('01.txt').readlines()

left = []
right = []

for l in lines:
    l, r = l.split()
    left.append(int(l))
    right.append(int(r))

left = sorted(left)
right = sorted(right)
cr = Counter(right)

s = 0
sim = 0

for idx, l in enumerate(left):
    s += abs(l - right[idx])
    sim += l * cr[l]

print("1:", s)
print("2:", sim)
