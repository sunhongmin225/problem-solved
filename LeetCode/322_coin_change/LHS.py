class Solution:
    # from https://velog.io/@bye9/LeetCode%ED%8C%8C%EC%9D%B4%EC%8D%AC-322.-Coin-Change
    def coinChange(self, coins: List[int], amount: int) -> int:
        d=[2**31-1]*(amount+1)
        d[0]=0
        for coin in coins:
            for i in range(coin, amount+1):
                d[i]=min(d[i], d[i-coin]+1)
        
        if d[amount]==(2**31-1):
            return -1
        
        return d[amount]

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if(amount==0):
#             return 0
        
#         self.change = 0
#         self.minChange = 2**31-1
#         self.findMinChange(coins, amount, self.minChange, self.change)
#         if(self.minChange == 2**31-1):
#             return -1
    
#         return self.minChange
    
#     def findMinChange(self, coins, amount, minChange, change):
#         if(amount <0):
#             return
#         if(amount==0):
#             self.minChange = min(minChange, change)
#             return
#         for i in range(len(coins)):
#             self.findMinChange(coins, amount-coins[i], minChange, change+1)
        
        #         if(amount==0):
#             return 0
#         if amount in coins:
#             return 1
        
#         #tgt = [x for x in coins if x<amount]
#         tgt = sorted(tgt, reverse=True)
#         # print("tgt:"+str(tgt))
#         total = 100000
#         flag = 
#         for i in range(len(tgt)):
#             #print("in loop: "+str(tgt[i]))
#             if( amount-tgt[i] >=0 ):
#                 temp = self.coinChange(coins, amount-tgt[i])
#                 # print("temp is "+str(temp))
#                 if(temp != 100000):
#                     total = min(total, temp+1)
#                 # print("total is "+str(total))
#         if(total == 100000):
#             return -1
#         return total
#     def 
        
        
#     def printint(self, coins):
#         print(coins)
        
        #         if (amount==0):
#             total = 0
#         else:
#             tgt = [x for x in coins if x<amount]
#             tgt = sorted(tgt, reverse=True)
#             total = 0
#             tamount = amount
#             for i in range(len(tgt)):
#                 q = int(tamount / tgt[i])
#                 r = tamount % tgt[i]
#                 tamount = r
#                 print("tamount: "+ str(tamount))       
#                 print("num: " + str(tgt[i]))
#                 print("q: " + str(q))
#                 print("r: " + str(r))
#                 if (r==0):
#                     total = q
#                     break

#                 for j in range(i+1, len(tgt)):
#                     qq = int(tamount / tgt[j])
#                     rr = tamount % tgt[j]
                    

#         return total