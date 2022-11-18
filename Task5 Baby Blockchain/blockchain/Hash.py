class Hash:
    def __init__(self) -> None:
        hash  = self.hash
        
    # Adds 0's for full seeing 512 bit number
    # @param pBits, whose will add zeros
    # @return pBits, number with zeros already added
    def addFullBits(pBits):
        while len(pBits)%512 != 448:
            pBits+="0"
        return pBits
        
    # Add big endian number in end
    # @param pBits, 512, whose will add little endian number and 512, it's size
    # @return pBits, number with little endian already added
    def chunks(l, n):
            return [l[i:i+n] for i in range(0, len(l), n)]

    # Edit index in end number
    # @param l whose will add index
    # @return number whose will add index
    def rol(n, b):
            return ((n << b) | (n >> (32 - b))) & 0xffffffff

    # HASH sha1
    # @param data, text whose will hashing
    # @return hash text
    def toSHA1(data):
        bytes = ""

        h0 = 0x67452301
        h1 = 0xEFCDAB89 
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0

        for n in range(len(data)):
            bytes+='{0:08b}'.format(ord(data[n]))

        bits = bytes+"1"
        pBits = bits
        pBits = Hash.addFullBits(pBits)
        pBits+='{0:064b}'.format(len(bits)-1)
        
        for c in Hash.chunks(pBits, 512): 
            words = Hash.chunks(c, 32)
            w = [0]*80
            for n in range(0, 16):
                w[n] = int(words[n], 2)
            for i in range(16, 80):
                w[i] = Hash.rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  
            a = h0
            b = h1
            c = h2
            d = h3
            e = h4
            #Main loop
            for i in range(0, 80):
                if 0 <= i <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i <= 59:
                    f = (b & c) | (b & d) | (c & d) 
                    k = 0x8F1BBCDC
                elif 60 <= i <= 79:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                temp = Hash.rol(a, 5) + f + e + k + w[i] & 0xffffffff
                e = d
                d = c
                c = Hash.rol(b, 30)
                b = a
                a = temp
            h0 = h0 + a & 0xffffffff
            h1 = h1 + b & 0xffffffff
            h2 = h2 + c & 0xffffffff
            h3 = h3 + d & 0xffffffff
            h4 = h4 + e & 0xffffffff
        return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

