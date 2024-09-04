import sys

def str_to_list(msg):
    msg = msg[2:] if msg.startswith('0x') else msg
    return [int(msg[i:i + 2], 16) for i in range(0, len(msg), 2)]


def KSA(key):
    j = 0
    s = list(range(256))
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def PRGA(s):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        yield s[(s[i] + s[j]) % 256]


def encrypt_decrypt(data, key):
    key_list = str_to_list(key)
    s = KSA(key_list)
    prga = PRGA(s)
    data_list = str_to_list(data)
    result = [(byte ^ next(prga)) for byte in data_list]
    return '0x' + ''.join(f'{byte:02x}' for byte in result)


def encrypt_stream(key: str):
    key_list = str_to_list(key)
    s = KSA(key_list)
    prga = PRGA(s)

    sys.stdin.read(2)
    sys.stdout.write('0x')

    while True:
        c = sys.stdin.read(1)
        if not c or c in '\n\r':
            break
        d = sys.stdin.read(1)
        byte = int(c + d, 16)
        sys.stdout.write(f'{byte ^ next(prga):02x}')


def main():
    key = input().strip()
    encrypt_stream(key)


if __name__ == "__main__":
    main()
