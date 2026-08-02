class StockSpanner:

    def __init__(self):
        self.prices = []
        
    def next(self, price: int) -> int:
        # print("prices: ",self.prices)
        # print("price: ", price)
        self.prices.append(price)
        # print("prices1: ",self.prices)
        span = 1
        index = len(self.prices)-2
        # print("index: ", index)
        # print("index > 0 and self.prices[index] <= price: ", index > 0 and self.prices[index] <= price)
        while index >= 0 and self.prices[index] <= price:
            # print("span: ", span)
            span+=1
            # print("afterspan: ", span)
            # print("beindex: ", index)
            index -=1
            # print("afindex: ", index)
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)