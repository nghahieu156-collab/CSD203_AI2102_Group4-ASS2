class CustomerNode:
    def __init__(self, ccode, cus_name, phone):
        self.ccode    = ccode
        self.cus_name = cus_name
        self.phone    = phone
        self.next     = None

    def __str__(self):
        return f"[{self.ccode}] {self.cus_name} | phone={self.phone}"


class CustomerList:
    def __init__(self):
        self.head = None

    def _exists(self, ccode):
        cur = self.head
        while cur:
            if cur.ccode == ccode:
                return True
            cur = cur.next
        return False