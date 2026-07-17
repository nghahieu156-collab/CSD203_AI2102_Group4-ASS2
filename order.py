""" 
Nguyen Tran Duc Minh 03/07/2026
"""
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
        new_node = OrderNode(pcode, ccode, quantity)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # ── 3.2 Display ───────────────────────────────────────
    def display(self):
        current = self.head
        while (current):
            print(current)
            current = current.next
            

    # ── 3.3 Sort by pcode + ccode (Bubble Sort) ───────────
    def sort_by_pcode_ccode(self):

        if not self.head:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                # Compare pcode; if they are equal, compare ccode.
                if (current.pcode > current.next.pcode) or (current.pcode == current.next.pcode
                                                            and current.ccode > current.next.ccode):
                    # swap code's value
                    current.pcode, current.next.pcode = current.next.pcode, current.pcode
                    current.ccode, current.next.ccode = current.next.ccode, current.ccode
                    current.quantity, current.next.quantity = current.next.quantity, current.quantity
                    swapped = True
                current = current.next

    # ── Lấy toàn bộ order (dùng cho Sales action) ─────────
    def get_all(self):
        orders = []
        current = self.head
        while current:
            orders.append(current)
            current = current.next
        return orders
        
    # ── Xóa order theo pcode + ccode (tuỳ chọn) ──────────
    def delete_order(self, pcode, ccode):
        if not self.head:
            return

        if self.head.pcode == pcode and self.head.ccode == ccode:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.pcode == pcode and current.next.ccode == ccode:
                current.next = current.next.next
                return
            current = current.next



