from Account import Account
from Signature import Signature
from Hash import Hash

class Operation: 
    # Due to the peculiarities of python, the "Operand" object can be replaced simply "self"
    def __init__(self, sender, receiver, amount, signature):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
    def printOperation(self):
        print(f"[->]Sender: {self.sender}\n[<-]Receiver: {self.receiver}\n[$]Amount: {self.amount} BT\n[🔒]Signature: {self.signature}")
    def verifyOperation(self):
        
        if Account.getBalanceFunc(self.sender) >= self.amount:
            print("[*]First verify: Done")
            if self.signature == True: 
                print("[*]Second verify: Done")
            else: 
                print("Error #2")
                print(self.signature)
        else:
            print("Error #1")
            print(Account.getBalanceFunc(self.sender), self.amount)

# print("[alert]Create new transaction")
# mount = 5
# сommission = mount*0.05
# senderPub = "ab6fa35427acf3a55a47284eec6e8702a1226c6d"
# sender =  Hash.toSHA1("ab6fa35427acf3a55a47284eec6e8702a1226c6d")
# receiver = "86460d9f38e774e3966bc19459634fa7e0e91bd6"

# transaction = Signature.signData(sender, mount, сommission)
# print(transaction)


# print(Signature.verifySignature(senderPub, mount, transaction, сommission))
# signature = Signature.verifySignature(senderPub, mount, transaction, сommission)

# operation = Operation(senderPub, receiver, mount, signature)
# operation.printOperation()
# operation.verifyOperation()  
