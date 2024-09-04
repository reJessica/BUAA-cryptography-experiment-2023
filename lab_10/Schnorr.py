import hashlib

def sha_1(text):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(text.encode('utf-8'))
    return sha1_hash.hexdigest()


def Mod_fast(a, b, p):
    tmp = a % p
    result = 1
    while b != 0:
        if b & 1 == 1:
            result = (result * tmp) % p
        b = b >> 1
        tmp = (tmp * tmp) % p
    return result


def sign(p, q, a, M, s, r):
    x = Mod_fast(a, r, p)
    S = M + str(x)
    e = int(sha_1(S), 16)
    y = (r + s * e) % q
    return e, y


def vrfy(p, a, M, v, e, y):
    x = Mod_fast(Mod_fast(a, y, p) * Mod_fast(v, e, p), 1, p)
    return e == int(sha_1(M + str(x)), 16)


def main():
    p = int(input())
    q = int(input())
    a = int(input())
    M = input()
    Mode = input()
    if Mode == 'Sign':
        s = int(input())
        r = int(input())
        e, y = sign(p, q, a, M, s, r)
        print(str(e) + " " + str(y))
    else:
        v = int(input())
        E = input()
        e, y = E.split()
        e = int(e)
        y = int(y)
        FLAG = vrfy(p, a, M, v, e, y)
        print(FLAG)


if __name__ == "__main__":
    main()
