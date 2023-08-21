import string
import secrets

def generate_random_string(length):
    char = string.ascii_letters + string.digits + "!@#$%^&*"
    strg = ''.join(secrets.choice(char) for _ in range(length))
    return strg

qanak = int(input("How many symbols do you need? "))

passw = generate_random_string(qanak)

lc = uc = d = p = 0

while True:
    lc = uc = d = p = 0  # Reset counts before each iteration
    for c in passw:
        if c in string.ascii_lowercase:
            lc += 1
        elif c in string.ascii_uppercase:
            uc += 1
        elif c in string.digits:
            d += 1
        elif c in string.punctuation:
            p += 1
    if lc >= 1 and uc >= 1 and d >= 1 and p >= 1:
        print(passw)
        break
    else:
        passw = generate_random_string(qanak)
