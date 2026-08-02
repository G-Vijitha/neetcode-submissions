class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)-1
        # print("n: ", n)
        max_area = 0
        for i in range(len(heights)):
            # print("i: ", i)
            cur_height = heights[i]
            # print("cur_height: ", cur_height)
            left = i
            # print("left: ", left)
            right = i
            # print("right: ", right)
            # print("left, heights[left-1], cur_height, left > 0 and heights[left-1]>= cur_height: ", left, heights[left-1], cur_height, left > 0 and heights[left-1]>= cur_height)
            while left > 0 and heights[left-1]>= cur_height:
                # print("insidewhileLeft: ", left)
                left -= 1
                # print("afterLeft: ", left)
            # print("right, len(heights) - 1, right < len(heights) - 1  and heights[right+1]>= cur_height: ", right, len(heights) - 1, right < 0 and heights[right+1]>= cur_height)
            # print("right < len(heights)-1 and heights[right + 1] >= cur_height: ", right < len(heights)-1 and heights[right + 1] >= cur_height)
            while right < len(heights)-1 and heights[right + 1] >= cur_height:
                # print("insideRight: ", right)
                right += 1
                # print("afterRight: ", right)
            # print("right, left: ", right, left)
            width = right - left +1
            # print("width: ", width)
            # print("cur_height, width: ", cur_height, width)
            area = cur_height * width
            # print("area: ", area)
            # print("max_area: ", max_area)
            max_area = max(max_area, area)
            # print("max_area1: ", max_area)
        return max_area
        