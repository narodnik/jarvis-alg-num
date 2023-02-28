def is_normal(f):
    a, b, c = f
    return -a < b <= a

def is_reduced(f):
    a, b, c = f
    return is_normal(f) and (a < c or (a == c and b >= 0))

def reduce(f):
    a, b, c = f
    while not is_reduced((a, b, c)):
        if a > c or (a == c and b < 0):
            a, b, c = c, -b, a
        elif a < c:
            if b <= -a:
                a, b, c = a, b + 2*a, c + b + a
            else:
                assert b > a
                a, b, c = a, b - 2*a, c - b + a
        else:
            assert a == c and b >= 0
            a, b, c = a, b - 2*a, c - b + a
    return a, b, c

assert is_reduced((1, 0, 13))
assert not is_reduced((1, 2, 14))

d = -13
if d % 4 in (2, 3):
    D = 4*d
else:
    D = d

reduced_forms = set()

for ac in range(-D/4, round(-D/3 + 1)):
    # b² - 4ac = D
    b2 = D + 4*ac
    if not b2.is_square():
        continue
    b = sqrt(b2)
    # 0 < a ≤ c
    print(ac)
    for a in range(1, ac):
        c = ac/a
        if a > c:
            break
        if not c in ZZ:
            continue
        c = int(c)

        f = reduce((a, b, c))
        reduced_forms.add(f)
        print(f"  {f}")

        f = reduce((a, -b, c))
        reduced_forms.add(f)
        print(f"  {f}")

print()
print(f"Class number = {len(reduced_forms)}")
