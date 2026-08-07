class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m × n)) / O(1)
        rows = len(matrix)
        # print("rows: ", rows)
        cols = len(matrix[0])
        # print("cols: ", cols)
        left = 0
        # print("left: ", left)
        right = rows * cols - 1
        # print("right: ", right)
        while left <= right:
            # print("l,r: ", left, right)
            mid = left + (right - left)//2
            # print("mid: ", mid)
            r = mid // cols
            # print("r: ", r)
            c = mid % cols
            # print("c:  ", c)
            val = matrix[r][c]
            # print("val: ", val)
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False






        # O(m log n)
        # for row in matrix:
        #     left = 0
        #     right = len(row)-1
        #     while left <= right:
        #         mid = left + (right - left)//2
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] < target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # return False



        #  O(m*n) / O(1)
        # for row in matrix:
        #     print("row: ", row)
        #     for num in row:
        #         print("num , row: ", num , row)
        #         if num == target:
        #             return True
        # return False