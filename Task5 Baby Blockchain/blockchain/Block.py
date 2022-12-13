from Hash import Hash
class Block: 
    global FullBlockList
    FullBlockList = []
    def __init__(self, blockID, prevHash, setOfTransactions): #create block
        self.blockID = Hash.toSHA1(blockID)
        self.prevHash = prevHash
        self.setOfTransactions = setOfTransactions
    def printBlock (self):
        print(f"blockID: {self.blockID}\nprevHash: {self.prevHash}\nsetOfTransactions: {self.setOfTransactions}")
    def addTransactionInBlock (self): 
        if len (FullBlockList) > 4: # max lengh in block == 4 transation
            Block.getBlockList(blockTrancation)
            return 0
        else: 
            FullBlockList.append([self.blockID, self.prevHash, self.setOfTransactions])
            return FullBlockList
    def getBlockList(blockTrancation):
        return blockTrancation
b = Block("aab3abb8a152dbfa2c1b73816a3404d207ac16ab", "aab3abb8a152dbfa2c1b73816a3404d207ac16ab", "3002")
blockTrancation = Block.addTransactionInBlock(b)
b1 = Block("c02ed5626c3fb6c3643e99917af6ae7bd7b6472f", "c02ed5626c3fb6c3643e99917af6ae7bd7b6472f", "3001")
blockTrancation = Block.addTransactionInBlock(b1)
b2 = Block("c02ed5626c3fb6c3643e99917af6ae7bd7b6472f", "c02ed5626c3fb6c3643e99917af6ae7bd7b6472f", "3001")
blockTrancation = Block.addTransactionInBlock(b2)
b3 = Block("c02ed5626c3fb6c3643e99917af6ae7bd7b6472f", "c02ed5626c3fb6c3643e99917af6ae7bd7b6472f", "3001")
blockTrancation = Block.addTransactionInBlock(b3)
b4 = Block("1S", "c02ed5626c3fb6c3643e99917af6ae7bd7b6472f", "3001")
blockTrancation = Block.addTransactionInBlock(b4)
Block.getBlockList(blockTrancation)
