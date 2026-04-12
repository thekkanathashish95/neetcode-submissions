class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left  = 1
        right = max(piles) ## Lowest possible speed we know of
        result = right  ## Possible speed. Defaults to lowest possible we know of

        while left <= right:
            speed = (left + right) // 2
            hours = 0
            for p in piles:
                hours+= math.ceil(p/speed)
            
            if hours<=h:
                result = speed ## new identified lower speed that satisfies requirement
                right = speed - 1

            else:
                left = speed + 1

        return result

         