from Hash import Hash

class KeyPair:

    def toString(text):
        return str(text)

    #use SHA-3
    #@param message -> whose will be generete key
    #@return hash massage
    def genKeyPair(data):
        privateKey = Hash.toSHA1(KeyPair.toString(Hash.toSHA1(KeyPair.toString(data))))
        publicKey = Hash.toSHA1(KeyPair.toString(data)) # In this way, we do 2-time hashing for security purposes.
        return privateKey, publicKey

    #Print key 
    #@param key massage
    def printKeyPair(privateKey, publicKey):
        print(f"privateKey: {privateKey}\npublicKey: {publicKey}")
        

