
class OrderNode:
    def __init__(self, pcode, ccode, quantity):
        self.pcode    = pcode    
        self.ccode    = ccode    
        self.quantity = quantity  
        self.next     = None

    def __str__(self):
        return (f"pcode: {self.pcode} | ccode: {self.ccode} | "
                f"quantity: {self.quantity}")


class LinkedListOrder:
    def __init__(self):
        self.head = None

    # ── 3.1 Input data (thêm order vào cuối) ─────────────
    def add_order(self, pcode, ccode, quantity):
        pass

    # ── 3.2 Display ───────────────────────────────────────
    def display(self):
        pass

    # ── 3.3 Sort by pcode + ccode (Bubble Sort) ───────────
    def sort_by_pcode_ccode(self):

        pass

    # ── Lấy toàn bộ order (dùng cho Sales action) ─────────
    def get_all(self):
        pass
    # ── Xóa order theo pcode + ccode (tuỳ chọn) ──────────
    def delete_order(self, pcode, ccode):
        pass



