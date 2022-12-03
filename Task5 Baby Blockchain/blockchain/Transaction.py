from random import randint
class Transaction:
    def __init__(self, transactionID, setOfOperations):
        self.nonce = randint(10000, 99999) # random number
        self.transactionID = transactionID
        self.setOfOperations = setOfOperations
        
    def printTransaction(self):
        print(f"nonce: {self.nonce}\ntransaction id: {self.transactionID}\nsetOfOperations: {self.setOfOperations}")
    
