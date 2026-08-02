class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        # print("pricee : ", price)
        span = 1
        # print("stack: ", self.stack)
        # print("span: ", span)
        # print("self.stack and self.stack[-1][0] <= price ", self.stack and self.stack[-1][0] <= price)
        while self.stack and self.stack[-1][0] <= price:
            # print("self.stack[-1]: ", self.stack[-1])
            # print("self.stack[-1][0]: ", self.stack[-1][0])
            # print("stack1: ", self.stack)
            prev_price, prev_span = self.stack.pop()
            # print("prev_price, prev_span: ", prev_price, prev_span)
            span = span + prev_span
        #     print("span2: ", span)
        # print("stack3: ", self.stack)
        self.stack.append((price, span))
        # print("lastSTACK: ", self.stack)
        return span

        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)