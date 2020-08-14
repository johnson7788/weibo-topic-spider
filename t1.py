import random
after = None
n = 0
while n < 5:
    before = after
    elems = random.choice([0,1,2,3])
    after = elems
    if before == after:
        n += 1
        print('n:',n)
        continue
    else:
        n = 0
    print("insert",elems)