class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            # print("###############################")
            # print("left, right: ", left, right)
            width = right - left
            # print("width: ", width)
            # print("heights[left], heights[right],min(heights[left], heights[right]: ", heights[left], heights[right],min(heights[left], heights[right]))
            water_ht = min(heights[left], heights[right])
            # print("water_ht: ", water_ht)
            current_water = width * water_ht
            # print("current_water: ", current_water)
            # print("current_water, max_water,current_water > max_water: ", current_water,max_water,current_water > max_water)
            if current_water > max_water:
                # print("Insidie IF")
                max_water = current_water
            #     print("max_water: ", max_water)
            # print("heights[left],heights[right],heights[left] < heights[right]: ", heights[left],heights[right],heights[left] < heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_water


        