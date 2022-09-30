# @author Borusov Illia
# @Version 1.0
import random


# Key generation in a range
# @param bits_range bit range
# @return key generated in a specific range
def generate(bits_range): 
    print("Key: ", random.randint(0, bits_range),"\n")

# Output number of key variants
# @param bits given bit rates
# @return number of key options
def print_options (bits):
    for i in range(len(bits)):
        print(bits[i],"- bit, Key options:", 2**bits[i])
        print('\n')
        generate(2**bits[i])

# Enter function
def main(): 
    bits = [8,16,32,64,128,256,512,1024,2048,4096]
    print_options(bits)

main()