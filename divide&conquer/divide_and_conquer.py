
def ekub(a, b):
    c = a - b
    print(f"{a} - {b} = {c}")
    if not c:
        return 1
    else:
        return 1 + ekub(b, c)

print(ekub(45, 27))

def ekub(a, b):
    c = a % b
    print(f"{a} % {b} = {c}")
    if not c:
        return 1
    else:
        return 1 + ekub(b, c)

print(ekub(45, 27))

def gcd(a,b):
    if a==0:
        return b
    if a>b:
        a,b=b,a
    return gcd(b-a,a)

print(gcd(45,27))

def gcd(a,b):
    if a==0:
        return b
    if a>b:
        a,b=b,a
    return gcd(b-a,a)

print(gcd(45,27))
