class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        # print("pairs", pairs)
        for charc in s:
            # print("charc", charc)
            if charc in "({[":
                stack.append(charc)
                # print("stack", stack)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                # print("top", top)
                # print("\n pairs[charc]", pairs[charc])
                if top != pairs[charc]:
                    return False
        return len(stack) == 0
        