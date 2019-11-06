#! /usr/bin/env python3 -u

import random
for round in range(10):
    a = random.randint(0, 10**100)
    b = random.randint(0, 10**100)
    print('%d + %d = ?' % (a, b));
    c = int(input())
    if a + b != c:
        break

print(open('flag.txt').read())
