from Hash import Hash
import json
import datetime
from Account import Account
class Signature: 

    def signData(privateKey, mount, сommission):
        sign = Hash.toSHA1(f"User {privateKey} send {mount} + сommission {сommission}")
        return sign

    def verifySignature(publicKey, mount, signature, сommission):
        sign = Hash.toSHA1(f"User {Hash.toSHA1(publicKey)} send {mount} + сommission {сommission}")
        if sign == signature :

            # now = datetime.datetime.now()
    
            # transaction = signature
            # data = {
            #     "version": 1,
            #     "time": now.isoformat(),
            #     "vin":[
            #         {
            #             "hash": transaction,
            #             "index": 0,
            #             "scriptSig": "True"
            #         },
            #     ],
            #     "vout":[
            #         {
            #             "value": mount,
            #             "scriptPubKey": publicKey,
            #         },
            #         {
            #             "value": mount+сommission,
            #             "scriptPubKey": publicKey,
            #         }
            #     ]
            # }

            # with open(f"./transaction/{transaction}.json", "w") as write_file:
            #     json.dump(data, write_file)
            #     Account.updateBalance(mount, publicKey, сommission)
            print("[->]send commission: ",сommission, "BT")

            return True 
        else: 
            return False

    def printSignature(signature):
        print(signature)


