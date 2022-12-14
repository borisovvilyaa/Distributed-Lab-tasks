class BlockChain(object): 
    def  __init__(self, block):
        self.block = block
        self.verifyBlocks = []
        BlockChain.verify(self)

    def addBlockToHistory(self):
        print("done, add new transaction")
        block = self.block
        self.verifyBlocks.append(block)
        BlockChain.verifyblock(self)
        #add to json 
    def verifyblock(self):
        print ("\n",self.verifyBlocks[0][1],"\n") #examination, if block have #1 block 
    def verify(self):
        for i in range(0,4):
            if self.block[i][0] == self.block[i-1][1]:
                if self.block[i][2]['Sign'] == True: 
                    if self.block[i][0] != self.block[i][1]: 
                        print("ok")
                        self.block[i][3]['coinDatabase'] = self.block[i][2]['send'] + self.block[i-1][3]['coinDatabase']
                        print ("coinbase: ",self.block[i])
                        BlockChain.addBlockToHistory(self)
                        
                    
                    
            else:
                print("no")
                
            
block = [
    [
        "1ca375538ac36c6febabde68f539e1ff2b683ba4",
        "aab3abb8a152dbfa2c1b73816a3404d207ac16ab",
        {
            "Sign": True,
            "send": 24.05
        },
        {
            "coinDatabase": 0
        }
    ],
    [
        "aab3abb8a152dbfa2c1b73816a3404d207ac16ab",
        "ce0b3dc9ea8c6adad3b7ffe7acb153a2584c0c8d",
        {
            "Sign": True,
            "send": 2.05
        },
        {
            "coinDatabase": 0
        }
    ]
    ,
    [
        "ce0b3dc9ea8c6adad3b7ffe7acb153a2584c0c8d",
        "aab3abb8a152dbfa2c1b73816a3404d207ac16ab",
        {
            "Sign": True,
            "send": 6.05
        },
        {
            "coinDatabase": 0
        }
    ],
    [
        "ce0b3dc9ea8c6adad3b7ffe7acb153a2584c0c8d",
        "ce0b3dc9ea8c6adad3b7ffe7acb153a2584c0c8d",
        {
            "Sign": True,
            "send": 12.05
        },
        {
            "coinDatabase": 0
        }
    ]
]#some chain of block
blockNew = BlockChain(block)
