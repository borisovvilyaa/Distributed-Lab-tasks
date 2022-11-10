class Crypto:
    def VigenereCipher(message, key):
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in message]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext

    def RSA (msg):
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
            
        def extendGcd(a, b): # The extended Euclid algorithm is a special case
            if b == 0:
                x = 1
                y = 0
                return x, y
            else:
                x1, y1 = extendGcd(b, a % b)
                x = y1
                y = x1 - (int)(a / b) * y1
                return x, y
            
        def fastMul(a,b,n):
            res=1
            while b!=0:
                if b%2==0:
                    b=b/2
                    a=(a*a)%n
                elif b%2!=0:
                    b=b-1
                    res=(res*a)%n
            return res

        def generateKey(p, q):
            n = p * q  
            fn = (p - 1) * (q - 1)     
            e = 7
            x, y = extendGcd(e, fn) 
            if x < 0:
                x = x + fn
            d = x
            return (n, e)

        def encrypt(m, publicKey):
            n = publicKey[0]
            e = publicKey[1]
            c = fastMul(m, e, n)
            return c


        def rsa_generate(msg):
            p = 3
            q = 11
            publicKey = generateKey(p, q)
            return encrypt(msg, publicKey)

        return rsa_generate(msg)


