class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        emptyBottles = 0
        extraBottles = 0
        numExchange = numExchange
        drankedBottles = 0

        while fullBottles > 0:
            drankedBottles += fullBottles
            emptyBottles = fullBottles + extraBottles
            fullBottles = 0
            while emptyBottles >= numExchange:
                fullBottles += 1
                emptyBottles -= numExchange
                numExchange += 1
            extraBottles = emptyBottles
        
        return drankedBottles