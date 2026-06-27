class CustomerNode:
    def __init__(self, ccode, cus_name, phone):
        self.ccode    = ccode      # unique key
        self.cus_name = cus_name
        self.phone    = phone      # chỉ chứa chữ số
        self.next     = None

    def __str__(self):
        return f"[{self.ccode}] {self.cus_name} | Phone: {self.phone}"


class LinkedListCustomer:
    def __init__(self):
        self.head = None

    # ── Validate ──────────────────────────────────────────
    def _is_valid_phone(self, phone):
        return phone.isdigit()

    def _ccode_exists(self, ccode):
        return self.search(ccode) is not None

    # ── 2.2 Add to end ────────────────────────────────────
    def add_to_end(self, ccode, cus_name, phone):
        pass
    # ── 2.3 Display ───────────────────────────────────────
    def display(self):
        pass

    # ── 2.5 Search by ccode ───────────────────────────────
    def search(self, ccode):
        pass

    # ── 2.6 Delete by ccode ───────────────────────────────
    def delete(self, ccode):
        pass

    # ── 2.1 Load từ file ──────────────────────────────────
    def load_from_file(self, filename="customers.txt"):
        pass

    # ── 2.4 Save to file ──────────────────────────────────
    def save_to_file(self, filename="customers.txt"):
        pass



