import binascii
import sys


def pad(mystr, size):
  padding_size=2*size
  mystr = mystr + "0"*(padding_size - len(mystr))
  return mystr

def generate(a, size):
    a=pad(a[:2*size], size)
    a1=int.from_bytes(binascii.unhexlify(a),byteorder='little')
    a2=int.from_bytes(binascii.unhexlify(a),byteorder='big')
    print(f"Value: 0x{a}\nNumber of bytes: {size}\nLittle-endian: {a1}\nBig-endian: {a2}")
    print("-*"*20,"\n")

def main(): 
    a= ["ff", "aaaa", "FFFFFFFF", "F"]
    size= [32, 32, 4, 512]
    for i in range (len(a)):
        generate(a[i], size[i])


if __name__ == "__main__":
    main()