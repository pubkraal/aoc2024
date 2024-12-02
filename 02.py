def is_safe(nums):
    prev = None
    asc = None
    for num in nums:
        if prev is None:
            prev = num
            continue

        if asc is None:
            asc = num > prev

        diff = abs(prev-num)
        if diff == 0:
            break
        if diff > 3:
            break
        if asc and num < prev:
            break
        if not asc and prev < num:
            break
        prev = num
    else:
        return True
    return False

with open("02.txt") as rd:
    p1 = 0
    p2 = 0
    for line in rd.readlines():
        nums = [int(x) for x in line.split()]
        if is_safe(nums):
            p1 += 1
        else:
            ln = len(nums)
            for i in range(ln):
                nn = nums[0:i] + nums[i+1:ln]
                if is_safe(nn):
                    p2 += 1
                    break
    print("1:", p1)
    print("2:", p1 + p2)
