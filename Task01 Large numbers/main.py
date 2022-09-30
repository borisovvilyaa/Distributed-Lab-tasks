# @author Borusov Illia
# @Version 0.2
import random
import datetime

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
        bits_options =  2**bits[i]
        print(bits[i],"- bit, Key options:",bits_options)
        generate(bits_options)

# Enter function
def main(): 
    bits = [8,16,32,64,128,256,512,1024,2048,4096]
    print_options(bits)

main()

# Code snippet to show code execution time
# start = datetime.datetime.now()
# end = datetime.datetime.now()
# print('totally time is ', end - start, '\n')