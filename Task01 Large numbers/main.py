# @author Borusov Illia
# @Version 0.3
import random
import time

# Brut-force key
# @param key generation in a range
# @return brut_force_key with the previous value of the found key
# @return duration time finding the key
def brute_force(key): 
    start = time.perf_counter_ns()
    brute_force_key = 0
    while True:
        if (brute_force_key != key):
            brute_force_key=brute_force_key+1
        else: 
            print("Brute-force key: ", brute_force_key) 
            duration = time.perf_counter_ns() - start
            print(f"The key was found in {duration // 1000000}ms.\n")
            break

# Key generation in a range
# @param bits_range bit range
# @return key generated in a specific range
def generate(bits_range): 
    key = random.randint(0, bits_range)
    print("Key: ", key)
    brute_force(key-1)
   
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

if __name__ == "__main__":
    main()