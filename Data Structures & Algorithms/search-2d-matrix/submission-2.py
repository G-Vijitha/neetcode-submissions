class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m log n)
        for row in matrix:
            left = 0
            right = len(row)-1
            while left <= right:
                mid = left + (right - left)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False



        #  O(m*n) / O(1)
        # for row in matrix:
        #     print("row: ", row)
        #     for num in row:
        #         print("num , row: ", num , row)
        #         if num == target:
        #             return True
        # return False