class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        # print("left, right, h : ", left,right, h)
        ans = right
        # print("ans: ", ans)
        while left <= right:
            # print("#####################################")
            # print("left1, right1: ", left,right)
            mid = left + (right-left)//2
            # print("mid, : ", mid)
            hours = 0
            # print("hours: ", hours)
            for pile in piles:
                # print("-------------------")
                # print("pile, : ", pile)
                hours += (pile + mid - 1) // mid
                # print("hours1: ", hours)
            if hours <= h:
                ans = mid
                # print("ans1: ", ans)
                # print("befreright3: ", right)
                right = mid - 1
                # print("afterright3: ", right)
            else:
                # print("befreleftt3: ", left)
                left = mid + 1
                # print("afterleftt3: ", left)
        return ans










        # O(n*m)
        # for speed in range(1, max(piles)+1):
        #     # print("#####################")
        #     # print("speed: ", speed)
        #     # print("spemax(piles): ", max(piles))
        #     hours = 0
        #     for pile in piles:
        #         # print("pile: ", pile)
        #         # print("hours: ", hours)
        #         # print("speedFOr: ", speed)
        #         # print("(pile + speed - 1)//speed: ", (pile + speed - 1)//speed)
        #         hours = hours + (pile + speed - 1)//speed
        #         # print("hours2: ", hours)
        #     if hours <= h:
        #         return speed
        