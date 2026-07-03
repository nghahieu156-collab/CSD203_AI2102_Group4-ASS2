"""
Nguyen Tran Duc Minh
"""

import tkinter as tk
from tkinter import ttk, messagebox

# --- OrderNode Class ---
class OrderNode:
    def __init__(self, pcode, ccode, quantity):
        self.pcode = pcode
        self.ccode = ccode
        self.quantity = quantity
        self.next = None

# --- LinkedListOrder Class ---
class LinkedListOrder:
    def __init__(self):
        self.head = None

    def add_order(self, pcode, ccode, quantity):
        new_node = OrderNode(pcode, ccode, quantity)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def sort_by_pcode_ccode(self):
        if not self.head or not self.head.next:
            return
        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            while curr.next:
                if (curr.pcode > curr.next.pcode) or \
                   (curr.pcode == curr.next.pcode and curr.ccode > curr.next.ccode):
                    curr.pcode, curr.next.pcode = curr.next.pcode, curr.pcode
                    curr.ccode, curr.next.ccode = curr.next.ccode, curr.ccode
                    curr.quantity, curr.next.quantity = curr.next.quantity, curr.quantity
                    swapped = True
                curr = curr.next

# --- Main Application UI ---
class OrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Order Management System")
        self.root.geometry("800x600")
        self.ll = LinkedListOrder()

        # Input Frame
        input_frame = tk.LabelFrame(self.root, text="Order Information", padx=10, pady=10)
        input_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(input_frame, text="Product Code:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_pcode = tk.Entry(input_frame)
        self.ent_pcode.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Customer Code:").grid(row=0, column=2, padx=5, pady=5)
        self.ent_ccode = tk.Entry(input_frame)
        self.ent_ccode.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
        self.ent_quantity = tk.Entry(input_frame)
        self.ent_quantity.grid(row=1, column=1, padx=5, pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Order", command=self.add_order_action).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Sort Data", command=self.sort_order_action).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Refresh Table", command=self.refresh_table).pack(side="left", padx=10)

        # Treeview Display
        self.tree = ttk.Treeview(self.root, columns=("P", "C", "Q"), show='headings')
        self.tree.heading("P", text="Product Code")
        self.tree.heading("C", text="Customer Code")
        self.tree.heading("Q", text="Quantity")
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

    def add_order_action(self):
        try:
            p = self.ent_pcode.get()
            c = self.ent_ccode.get()
            q = int(self.ent_quantity.get())
            if not p or not c:
                raise ValueError
            
            self.ll.add_order(p, c, q)
            self.refresh_table()
            messagebox.showinfo("Success", "Order added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data in all fields!")

    def sort_order_action(self):
        self.ll.sort_by_pcode_ccode()
        self.refresh_table()
        messagebox.showinfo("Success", "List sorted by Product and Customer code!")

    def refresh_table(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Traverse Linked List and insert into Treeview
        curr = self.ll.head
        while curr:
            self.tree.insert("", "end", values=(curr.pcode, curr.ccode, curr.quantity))
            curr = curr.next

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderApp(root)
    root.mainloop()
