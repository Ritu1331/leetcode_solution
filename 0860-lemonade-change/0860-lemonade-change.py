class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n = len(bills)
        five = 0
        ten = 0
        for i in range(n):
            money = bills[i]
            if (money == 5):
                five += 1
            elif(money == 10):
                if (five == 0):
                    return False
                
                else:
                    five -= 1
                    ten += 1
            
            else: #(money == 20)
                if(ten > 0):
                    ten -= 1
                    if (five == 0):
                        return False
                    
                    else:
                        five -= 1
                
                else:
                    if (five < 3):
                        return False
                    
                    else:
                        five = five - 3
        return True



        