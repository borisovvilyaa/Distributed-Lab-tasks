# @author Borusov Illia
# @Version 1.0

def print_options (bits):
    for i in range(len(bits)):
        print(2**bits[i])
        print('\n')

def main(): 
    bits = [8,16,32,64,128,256,512,1024,2048,4096]
    print_options(bits)

main()