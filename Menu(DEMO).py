"""
Name: Tran Khac Viet
Date: 02/07/2026
Description:
"""
╔══════════════════════════════════════════════════════════╗
║   SALES AND INVENTORY MANAGEMENT SYSTEM (SIMS)          ║
║   DSA Assignment 2 – CSD203                             ║
╠══════════════════════════════════════════════════════════╣
║  Team members:                                          ║
║    Hieu  – Products (BST)                               ║
║    Son   – Customers (Linked List)                      ║
║    Minh  – Orders (Linked List)                         ║
║    Viet  – Sales Action + Main Menu                     ║
╚══════════════════════════════════════════════════════════╝

Run command: python main_menu.py
"""

# Import modules from team members
# Each file is located in the same directory as main_menu.py

from Products   import ProductBST                          # Product BST (Hieu)
from Customers   import CustomerList, customer_menu         # Customer linked list (Son)
from order      import LinkedListOrder                     # Order linked list (Minh)
from Sales import sales_menu                       # Sales action (Viet)


# ══════════════════════════════════════════════════════════════
# SUB MENU: 1. PRODUCTS  
# ══════════════════════════════════════════════════════════════

def product_menu(bst):
    """
    Sub menu for section 1 – Products (BST).
    Calls methods of the ProductBST class written by Hieu.
    """
    MENU = """
╔══════════════════════════════════════════════════╗
║         1. PRODUCTS (Binary Search Tree)         ║
╠══════════════════════════════════════════════════╣
║  1.1  Load data from file                       ║
║  1.2  Enter & add product                       ║
║  1.3  In-order traversal (by pcode ascending)    ║
║  1.4  Breadth-first traversal (BFS by level)    ║
║  1.5  Save In-order to file                     ║
║  1.6  Search by pcode                           ║
║  1.7  Delete by pcode (copy method)             ║
║  1.8  Simple balance the BST                    ║
║  1.9  Count number of products                  ║
║  0.   Back to main menu                         ║
╚══════════════════════════════════════════════════╝"""

    while True:
        print(MENU)
        choice = input("Select function: ").strip()

        # 1.1 Load data from file
        if choice == "1.1":
            filepath = input("File path: ").strip()
            loaded = 0
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    for line_no, line in enumerate(f, start=1):
                        line = line.strip()
                        if not line:
                            continue
                        parts = [p.strip() for p in line.split(",")]
                        # Each line format: pcode,pro_name,quantity,saled,price
                        if len(parts) != 5:
                            print(f"[!] Line {line_no} has incorrect format, skipped: {line}")
                            continue
                        pcode, pro_name, quantity, saled, price = parts
                        ok = bst.insert(pcode, pro_name, quantity, saled, price)
                        if ok:
                            loaded += 1
                        else:
                            print(f"[!] pcode '{pcode}' already exists, skipped.")
                print(f"Loaded {loaded} products from '{filepath}'.")
            except FileNotFoundError:
                print(f"[!] File not found: {filepath}")

        # 1.2 Enter & add product
        elif choice == "1.2":
            pcode    = input("Product code (pcode)   : ").strip()
            pro_name = input("Product name           : ").strip()
            try:
                quantity = int(input("Quantity in stock     : ").strip())
                saled    = int(input("Quantity sold         : ").strip())
                price    = float(input("Price (VND)           : ").strip())
            except ValueError:
                print("[!] Invalid quantity/price.")
                continue
            if saled > quantity:
                print("[!] Sold quantity cannot exceed stock quantity.")
                continue
            ok = bst.insert(pcode, pro_name, quantity, saled, price)
            if ok:
                print(f"Product [{pcode}] added successfully.")
            else:
                print(f"[!] pcode '{pcode}' already exists. Not added.")

        # 1.3 In-order
        elif choice == "1.3":
            nodes = bst.inorder()
            if not nodes:
                print("Tree is empty.")
            else:
                print(f"\n{'pcode':<10}{'Product name':<25}{'Qty':>6}{'Sold':>8}{'Remain':>8}{'Price':>12}")
                print("-" * 72)
                for n in nodes:
                    print(f"{n.pcode:<10}{n.pro_name:<25}{n.quantity:>6}"
                          f"{n.saled:>8}{n.remaining():>8}{n.price:>11,.0f}")
                print(f"\nTotal: {len(nodes)} products")

        # 1.4 BFS
        elif choice == "1.4":
            nodes = bst.bfs()
            if not nodes:
                print("Tree is empty.")
            else:
                print("\nBFS traversal (level order):")
                print(f"{'pcode':<10}{'Product name':<25}{'Qty':>6}{'Sold':>8}{'Remain':>8}{'Price':>12}")
                print("-" * 72)
                for n in nodes:
                    print(f"{n.pcode:<10}{n.pro_name:<25}{n.quantity:>6}"
                          f"{n.saled:>8}{n.remaining():>8}{n.price:>11,.0f}")

        # 1.5 Save In-order to file
        elif choice == "1.5":
            filepath = input("Save to file (path): ").strip()
            nodes = bst.inorder()
            with open(filepath, "w", encoding="utf-8") as f:
                for n in nodes:
                    f.write(f"{n.pcode},{n.pro_name},{n.quantity},{n.saled},{n.price}\n")
            print(f"Saved {len(nodes)} products to '{filepath}'.")

        # 1.6 Search by pcode
        elif choice == "1.6":
            pcode = input("Enter pcode to search: ").strip()
            node = bst.search(pcode)
            if node:
                print(f"\nFound: {node}")
            else:
                print(f"pcode '{pcode}' not found.")

        # 1.7 Delete by pcode
        elif choice == "1.7":
            pcode = input("Enter pcode to delete: ").strip()
            ok = bst.delete(pcode)
            if ok:
                print(f"Product '{pcode}' deleted.")
            else:
                print(f"pcode '{pcode}' not found.")

        # 1.8 Balance tree
        elif choice == "1.8":
            bst.balance()
            print("BST balanced successfully.")

        # 1.9 Count products
        elif choice == "1.9":
            total = bst.count()
            print(f"Total products in BST: {total}")

        elif choice == "0":
            print("Returning to main menu...")
            break

        else:
            print("[!] Invalid choice.")


# ══════════════════════════════════════════════════════════════
# SUB MENU: 3. ORDER LIST  
# ══════════════════════════════════════════════════════════════

def order_menu(ll_order):
    """
    Sub menu for section 3 – Order List.
    Calls methods of the LinkedListOrder class written by Minh.
    """
    MENU = """
╔══════════════════════════════════════════════════╗
║         3. ORDER LIST                            ║
╠══════════════════════════════════════════════════╣
║  3.1  Add new order                             ║
║  3.2  Display order list                        ║
║  3.3  Sort by pcode + ccode                      ║
║  0.   Back to main menu                         ║
╚══════════════════════════════════════════════════╝"""

    while True:
        print(MENU)
        choice = input("Select function: ").strip()

        if choice == "3.1":
            pcode = input("Product code (pcode): ").strip()
            ccode = input("Customer code (ccode): ").strip()
            try:
                qty = int(input("Quantity: ").strip())
            except ValueError:
                print("[!] Quantity must be an integer.")
                continue
            ll_order.add_order(pcode, ccode, qty)
            print("Order added.")

        elif choice == "3.2":
            ll_order.display()

        elif choice == "3.3":
            ll_order.sort_by_pcode_ccode()
            print("Sorted. Displaying again:")
            ll_order.display()

        elif choice == "0":
            print("Returning to main menu...")
            break

        else:
            print("[!] Invalid choice.")


# ══════════════════════════════════════════════════════════════
# MAIN MENU
# ══════════════════════════════════════════════════════════════

def main():
    """
    Main entry point of the program.
    Initializes the 3 data structures and displays the main menu.
    """

    # Initialize data structures
    bst      = ProductBST()       # BST containing products (Hieu)
    ll_cus   = CustomerList()     # Linked list of customers (Son)
    ll_order = LinkedListOrder()  # Linked list of orders (Minh)

    # Automatically load default customer file (if exists)
    ll_cus.load_from_file("customers.txt")

    # Main menu
    MAIN_MENU = """
╔══════════════════════════════════════════════════════════╗
║        SALES AND INVENTORY MANAGEMENT SYSTEM             ║
║         Sales and Inventory Management System            ║
╠══════════════════════════════════════════════════════════╣
║  1.  Products   (Binary Search Tree)                    ║
║  2.  Customers  (Customer List)                         ║
║  3.  Orders     (Order List)                            ║
║  4.  Sales Action (Sales transactions)                  ║
║  0.  Exit program                                       ║
╚══════════════════════════════════════════════════════════╝"""

    print("\n" + "═" * 58)
    print("  Welcome to SIMS (Group4) – CSD203 Assignment 2")
    print("═" * 58)

    while True:
        print(MAIN_MENU)
        choice = input("Select option: ").strip()

        if choice == "1":
            product_menu(bst)

        elif choice == "2":
            # Call customer_menu() directly from Son's module
            customer_menu(ll_cus)

        elif choice == "3":
            order_menu(ll_order)

        elif choice == "4":
            # Call sales_menu() from Viet – needs all three data structures
            sales_menu(bst, ll_cus, ll_order)

        elif choice == "0":
            print("\n Thank you for using SIMS. Goodbye!\n")
            break

        else:
            print("[!] Invalid choice. Please enter 0–4.")


# ── Run program ──
if __name__ == "__main__":
    main()
