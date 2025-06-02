import random
import math

def determinate_prime(number):

    if number < 2:
        return False
    limite = int(math.sqrt(number) + 1)
    for i in range(2, limite):
        if number % i == 0:
            return False
    return True

def Generate_prime_numbers(length):
    
    lower = 2**(length-1)
    upper = (2**length) - 1


    p = random.randrange(lower, upper)
    
    while not determinate_prime(p):
        p += 1

        if p > upper:
            p = random.randrange(lower, upper)
    return p

def egcd(a, b) -> tuple[int, int, int]:

    a, b = abs(a), abs(b)

    if a == 0:
        return (b, 0 ,1)
    
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b != 0:
        q = a // b

        a, b = b, a - q * b

        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return (a, x0, y0)

def modinv(e, phi):

    g, x, _ = egcd(e, phi)

    if g != 1:
        raise Exception('no son coprimos')
    return x % phi

def encrypt_rsa(message, public_key):

    e, n = public_key
    if message < 0 or message >= n:
        raise ValueError("dentro del rango porfa")
    
    ciphertext = pow(message, e, n)
    return ciphertext

def decrypy_rsa(ciphertext, private_key):

    d, n = private_key
    message = pow(ciphertext, d, n)
    return message

def main():
    print('Lets encrypt a text')

    p = Generate_prime_numbers(1024)
    q = Generate_prime_numbers(1024)

    n = p * q

    phi_n = (p - 1) * (q - 1)

    e = random.randrange(3, phi_n -1, 2)
    while math.gcd(e, phi_n) != 1:
        e = random.randrange(3, phi_n -1, 2)

    d = modinv(e, phi_n)

    public_key = e, n
    private_key = d, n

    texto = input('Que quieres codificar? ')

    menssage = int("".join(str(ord(c)).zfill(3) for c in texto))

    print(menssage)

    c = encrypt_rsa(menssage, public_key)
    

    m = decrypy_rsa(c, private_key)
    

    m_str = str(m)

    while len(m_str) % 3 != 0:
        m_str = '0' + m_str
    
    resultado = "".join(
        chr(int(m_str[i:i+3])) for i in range(0, len(m_str), 3)
    )
    print(resultado)

if __name__ == '__main__':
   main()   