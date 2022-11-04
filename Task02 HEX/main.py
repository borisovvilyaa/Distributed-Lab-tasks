import binascii

# Creates a 16-bit number with the desired length
# @param hex number, which we will set the desired length
# @param size number length
# @return hex а number with a given length 
def lengthGauge(hex, size):
    padding_size = 2 * size
    hex = hex + "0" * (padding_size - len(hex))
    return hex

# Conversion from numbers to hex
# @param littleEndian the number that we transform to hex
# @param bigEndian the number that we transform to hex
# @return littleEndian, bigEndian numbers in hex
def generateHex(littleEndian, bigEndian, size):
    littleEndianToHex = lengthGauge(hex(littleEndian).split("x")[-1], size)
    BigEndianToHex = lengthGauge(hex(bigEndian).split("x")[-1], size)
    print(f"Little-endian to HEX: 0x{littleEndianToHex}\nBig-endian to HEX: 0x{BigEndianToHex}")

# Converter with hex to Big-endian and Little-endian
# @param hexItem which was generated before
# @param size number length
# @return littleEndian, bigEndian numbers
def generate(hexItem, size):
    hexItem = lengthGauge(hexItem[: 2 * size], size)
    littleEndian = int.from_bytes(binascii.unhexlify(hexItem), byteorder="little")
    bigEndian = int.from_bytes(binascii.unhexlify(hexItem), byteorder="big")
    print(f"Value: 0x{hexItem}\nNumber of bytes: {size}\nHEX to Little-endian: {littleEndian}\nHEX to Big-endian: {bigEndian}")
    # print(f"Little-endian To hex: 0x{hexItem} \n Big-endian To hex: 0x{hexItem}")
    generateHex(littleEndian, bigEndian, size)
    print("-*" * 20, "\n")

# entry point
def main():
    hexItem = ["ff", "aaaa", "ffffffff", "f"]
    size = [32, 32, 4, 512]
    for i in range(len(hexItem)):
        generate(hexItem[i], size[i])


if __name__ == "__main__":
    main()