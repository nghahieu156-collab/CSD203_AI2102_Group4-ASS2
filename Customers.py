"""
Name: Pham Hai Son
Date: 01/07/2026
Description:
    Customer part - Sales and Inventory Management System
    Custom singly linked list.
    Covers menu:
    2.1 Load data from file
    2.2 Input & add to the end
    2.3 Display data
    2.4 Save customer list to file
    2.5 Search by ccode
    2.6 Delete by ccode 
"""

class CustomerNode:
    def __init__(self, ccode, cus_name, phone):
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone
        self.next = None

class CustomerList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # ---------- helpers ----------
    def _exists(self, ccode):
        cur = self.head
        while cur:
            if cur.ccode == ccode:
                return True
            cur = cur.next
        return False

    @staticmethod
    def _valid_phone(phone):
        return phone.isdigit()

    # ---------- 2.2 add to end ----------
    def add(self, ccode, cus_name, phone):
        if self._exists(ccode):
            print(f"[!] ccode '{ccode}' already exists. Not added.")
            return False
        if not self._valid_phone(phone):
            print(f"[!] phone '{phone}' invalid (digits only). Not added.")
            return False

        node = CustomerNode(ccode, cus_name, phone)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1
        return True

    def input_and_add(self):
        ccode = input("Customer code (ccode): ").strip()
        cus_name = input("Customer name: ").strip()
        phone = input("Phone (digits only): ").strip()
        self.add(ccode, cus_name, phone)

    # ---------- 2.3 display ----------
    def display(self):
        if self.head is None:
            print("Customer list empty.")
            return
        print(f"{'ccode':<10}{'cus_name':<20}{'phone':<15}")
        print("-" * 45)
        cur = self.head
        while cur:
            print(f"{cur.ccode:<10}{cur.cus_name:<20}{cur.phone:<15}")
            cur = cur.next
        print(f"Total customers: {self.count}")

    # ---------- 2.1 load from file ----------
    def load_from_file(self, filepath):
        loaded = 0
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) != 3:
                        print(f"[!] line {line_no} malformed, skipped: {line}")
                        continue
                    ccode, cus_name, phone = (p.strip() for p in parts)
                    if self.add(ccode, cus_name, phone):
                        loaded += 1
        except FileNotFoundError:
            print(f"[!] file not found: {filepath}")
            return 0
        print(f"Loaded {loaded} customers from {filepath}.")
        return loaded

    # ---------- 2.4 save to file ----------
    def save_to_file(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            cur = self.head
            while cur:
                f.write(f"{cur.ccode},{cur.cus_name},{cur.phone}\n")
                cur = cur.next
        print(f"Saved {self.count} customers to {filepath}.")

    # ---------- 2.5 search by ccode ----------
    def search(self, ccode):
        cur = self.head
        while cur:
            if cur.ccode == ccode:
                return cur
            cur = cur.next
        return None

    def search_and_print(self, ccode):
        node = self.search(ccode)
        if node:
            print(f"Found: {node.ccode} | {node.cus_name} | {node.phone}")
        else:
            print(f"ccode '{ccode}' not found.")
        return node

    # ---------- 2.6 delete by ccode ----------
    def delete(self, ccode):
        prev = None
        cur = self.head
        while cur:
            if cur.ccode == ccode:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self.count -= 1
                print(f"Deleted ccode '{ccode}'.")
                return True
            prev = cur
            cur = cur.next
        print(f"ccode '{ccode}' not found. Nothing deleted.")
        return False

# ---------------- menu ----------------
def customer_menu(clist):
    MENU = """
--- Customer List ---
2.1 Load data from file
2.2 Input & add to the end
2.3 Display data
2.4 Save customer list to file
2.5 Search by ccode
2.6 Delete by ccode
0. Back
"""
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "2.1":
            path = input("File path to load: ").strip()
            clist.load_from_file(path)
        elif choice == "2.2":
            clist.input_and_add()
        elif choice == "2.3":
            clist.display()
        elif choice == "2.4":
            path = input("File path to save: ").strip()
            clist.save_to_file(path)
        elif choice == "2.5":
            ccode = input("ccode to search: ").strip()
            clist.search_and_print(ccode)
        elif choice == "2.6":
            ccode = input("ccode to delete: ").strip()
            clist.delete(ccode)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    clist = CustomerList()
    # demo: load fake data if present
    clist.load_from_file("customers.txt")
    customer_menu(clist)
