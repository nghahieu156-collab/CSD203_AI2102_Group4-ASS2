from collections import deque

class ProductNode:
    def __init__(self, pcode, pro_name, quantity, saled, price):
        self.pcode    = pcode
        self.pro_name = pro_name
        self.quantity = int(quantity)
        self.saled    = int(saled)
        self.price    = float(price)
        self.left     = None
        self.right    = None

    def remaining(self):
        return self.quantity - self.saled

    def __str__(self):
        return (f"[{self.pcode}] {self.pro_name} | "
                f"qty={self.quantity} sold={self.saled} "
                f"remain={self.remaining()} price={self.price:.2f}")

class ProductBST:
    def __init__(self):
        self.root = None