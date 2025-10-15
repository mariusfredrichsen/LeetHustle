class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        newBottles = numBottles
        emptyBottles = 0
        extraBottles = 0
        drinkedBottles = 0

        while newBottles > 0:
            drinkedBottles += newBottles
            emptyBottles = newBottles + extraBottles
            newBottles = emptyBottles // numExchange
            extraBottles = emptyBottles % numExchange


        return drinkedBottles


