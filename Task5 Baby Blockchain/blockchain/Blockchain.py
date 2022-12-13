class BlockChain: 
    def  __init__(self, block):
        self.block = block
        BlockChain.verify(self)
    def addBlockToHistory(self):
        print("done, add new transaction")
        #add to json 
    def verify(self):
        
        for i in range(0,4):
            if self.block[i][0] == self.block[i-1][1]:
                print("ok")
                if self.block[i][2]['Sign'] == True: 
                    if self.block[i][2]['Sign'] != self.block[i][2]['Sign']: 
                        BlockChain.addBlockToHistory(self.block)
                    
                    
            else:
                print("no")
                
            
block = [
    [
        "1ca375538ac36c6febabde68f539e1ff2b683ba4",
        "aab3abb8a152dbfa2c1b73816a3404d207ac16ab",
        {
            "Sign": True,
            "send": 2.05
        }
    ],
    [
        "aab3abb8a152dbfa2c1b73816a3404d207ac16ab",
        "ce0b3dc9ea8c6adad3b7ffe7acb153a2584c0c8d",
        {
            "Sign": True,
            "send": 2.05
        }
    ]
    ,
    [
        "aab3abb8a152dbfa2c1b73816a3404d207ac16ab",
        "ce0b3dc9ea8c6adad3b7ffe7acb153a2584c0c8d",
        {
            "Sign": False,
            "send": 6.05
        }
    ],
    [
        "ce0b3dc9ea8c6adad3b7ffe7acb153a2584c0c8d",
        "ce0b3dc9ea8c6adad3b7ffe7acb153a2584c0c8d",
        {
            "Sign": False,
            "send": 6.05
        }
    ]
]
#some pool
blockNew = BlockChain(block)
