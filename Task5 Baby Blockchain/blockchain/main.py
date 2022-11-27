from KeyPair import *
from Signature import Signature
from WordGen import WordGen
from Account import Account

# create account and transaction
print("[alert]Generate words")
words = WordGen.wordGen()
WordGen.printGen(words)

print("Generate keys")
fullKey = KeyPair.genKeyPair(words)

privateKey = fullKey[0]
publicKey = fullKey[1]

KeyPair.printKeyPair(privateKey, publicKey)

print("[alert]Add new account")
newUser = Account(0, publicKey, 0)

newUser.createJson()

print("[alert]Create new transaction")
mount = 10
сommission = mount*0.05
transaction = Signature.signData(privateKey, mount, сommission)
print(transaction)


print(Signature.verifySignature(publicKey, mount, transaction, сommission))

# #sign in 
# Account.signIn()
