class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        # print("res: ", result)
        stack = []
        # print("st: ", stack)
        for cur_idx in range(n):
            # print("cur_idx: ", cur_idx)
            # print("lenstack: ", len(stack))
            
            while (len(stack) > 0 and temperatures[cur_idx] > temperatures[stack[-1]]):

                # print("temperatures[cur_idx] > temperatures[stack[-1]]:", temperatures[cur_idx] > temperatures[stack[-1]])
                # print("temperatures[cur_idx], temperatures[stack[-1]] ",temperatures[cur_idx], temperatures[stack[-1]])
                prev_idx = stack.pop()
                # print("prev_idx:", prev_idx)
                # print("cur_idxInside:", cur_idx)
                # print("result1: ", result)
                result[prev_idx] = cur_idx - prev_idx
                # print("result2: ", result)
                # print("stack1: ", stack)
            stack.append(cur_idx)
            # print("stack2: ", stack)
        return result
        