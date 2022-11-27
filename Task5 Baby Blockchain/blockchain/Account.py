import json
from Hash import Hash
class Account:
    #__init__ replaces function genAccount()
    
    def __init__ (self, accountID, wallet, balance):
        self.id = accountID
        self.wallet = wallet
        self.balance = balance
    
    def createJson(self):
        data = {
            "id": self.id,
            "wallet": self.wallet,
            "balance": self.balance,
        }
        with open(f"account/{self.wallet}.json", "w") as write_file:
            json.dump(data, write_file)

    def printAll(publicKey):
        with open(f'account/{publicKey}.json', 'r') as f:
                obj = json.load(f)
                print(f"id: {obj['id']} | wallet: {obj['wallet']} | balance: {obj['balance']}.0 BT")
    def addKeyPairToWallet():
        pass
    
    def updateBalance(mount, publicKey, сommission):
        with open(f'account/{publicKey}.json', 'r') as f:
                obj = json.load(f)

                obj["balance"] = obj["balance"]+mount
                print(f"[->]Account {publicKey} add: BT",obj["balance"])
                
                with open(f'account/{publicKey}.json', 'w') as f:
                    json.dump(obj, f)
        with open(f'account/86460d9f38e774e3966bc19459634fa7e0e91bd6.json', 'r') as f:
                obj = json.load(f)

                obj["balance"] = obj["balance"]+сommission
                
                
                with open(f'account/86460d9f38e774e3966bc19459634fa7e0e91bd6.json', 'w') as f:
                    json.dump(obj, f)
    

    def getBalance(self):
        return self.balance
    def getBalanceFunc(publicKey):
        with open(f'account/{publicKey}.json', 'r') as f:
                obj = json.load(f)
                return obj["balance"]
    def printBalance(publicKey):
        with open(f'account/{publicKey}.json', 'r') as f:
                obj = json.load(f)
                print(f"[->]Account {publicKey} balance: BT",obj["balance"])
    def signIn():
        password = str(input("Password (12 word): "))
        pubKey = str(input("Public Key: "))
        if Hash.toSHA1(password) == pubKey:
            print("[✅]Sign success")
            
            with open(f'account/{pubKey}.json', 'r') as f:
                obj = json.load(f)
                account = Account(obj['id'], obj['wallet'], obj['balance'])
                print(f"Total balance: {Account.getBalance(account)}.0 BT")
        else:
            print("Sign not success")
            Account.signIn()

    

