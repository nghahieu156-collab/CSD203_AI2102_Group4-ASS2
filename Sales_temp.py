"""
Name: Tran Khac Viet
Date: 02/07/2026
Description:
    Sales Action - Sales & Inventory Management System
    Covers menu:
        4.1 Register Sale
        4.2 Employees (ccode) with most sales
        4.3 Most sold items
"""

from datetime import datetime   # get current date/time when registering a sale


def register_sale(bst, ll_cus, ll_order):
    print("\n========== REGISTER SALE TRANSACTION ==========")

    # Check customer
    ccode = input("Enter customer code (ccode): ").strip()
    customer = ll_cus.search(ccode)          # search() function from Customers.py returns node or None
    if customer is None:
        print(f"[!] Customer code '{ccode}' does not exist. Transaction cancelled.")
        return False

    # Check product
    pcode = input("Enter product code (pcode): ").strip()
    product = bst.search(pcode)             # search() function from Products.py returns node or None
    if product is None:
        print(f"[!] Product code '{pcode}' does not exist. Transaction cancelled.")
        return False

    # Display product information for user reference
    print(f"    Product    : {product.pro_name}")
    print(f"    Stock      : {product.remaining()} (quantity={product.quantity}, sold={product.saled})")
    print(f"    Unit price : {product.price:,.0f} VND")

    # Check quantity
    try:
        qty = int(input("Quantity to buy: ").strip())
    except ValueError:
        print("[!] Quantity must be an integer. Transaction cancelled.")
        return False

    if qty <= 0:
        print("[!] Quantity must be greater than 0. Transaction cancelled.")
        return False

    # Check condition: saled + qty <= quantity
    if product.saled + qty > product.quantity:
        print(f"[!] Insufficient stock. Remaining stock: {product.remaining()}. Transaction cancelled.")
        return False

    # Update saled in BST
    ok, msg = bst.update_saled(pcode, qty)    # update_saled() function from Products.py
    if not ok:
        print(f"[!] Error updating stock: {msg}. Transaction cancelled.")
        return False

    # Add order to ll_order
    ll_order.add_order(pcode, ccode, qty)     # add_order() function from order.py

    # Print confirmation invoice
    now = datetime.now()
    # Auto-generate transaction ID from timestamp (e.g., TXN20260702153045)
    txn_id = "TXN" + now.strftime("%Y%m%d%H%M%S")
    total  = qty * product.price

    print("\n" + "─" * 50)
    print("          TRANSACTION INVOICE")
    print("─" * 50)
    print(f"  Transaction ID : {txn_id}")
    print(f"  Date/Time      : {now.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"  Customer       : {ccode}  ({customer.cus_name})")
    print(f"  Product        : [{pcode}] {product.pro_name}")
    print(f"  Quantity       : {qty}")
    print(f"  Unit price     : {product.price:,.0f} VND")
    print(f"  TOTAL          : {total:,.0f} VND")
    print("─" * 50)
    print("  Transaction successful! Thank you for your purchase.")
    print("─" * 50 + "\n")
    return True



def employees_most_sales(ll_order):
    print("\n========== STATISTICS BY CUSTOMER CODE ==========")

    # Get full list of orders (list of OrderNode)
    all_orders = ll_order.get_all()

    if not all_orders:
        print("No transactions have been recorded yet.")
        return

    # ── Accumulate quantity by ccode (without using Counter) ─────
    # Use a plain dict
    sales_dict = {}        # { ccode: total_quantity }
    for order in all_orders:
        ccode = order.ccode
        qty   = order.quantity
        if ccode in sales_dict:
            sales_dict[ccode] += qty
        else:
            sales_dict[ccode] = qty

    # ── Sort descending by total quantity (manual Bubble Sort) ──
    # Convert dict to list of tuples for sorting
    items = list(sales_dict.items())   # [ (ccode, total), ... ]

    # Bubble Sort descending by total (index 1)
    n = len(items)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    # Print result table
    print(f"\n{'Rank':<6}{'Customer (ccode)':<18}{'Total quantity sold':>20}")
    print("-" * 46)
    for rank, (ccode, total) in enumerate(items, start=1):
        marker = "   HIGHEST" if rank == 1 else ""
        print(f"{rank:<6}{ccode:<18}{total:>20}{marker}")
    print("-" * 46)
    print(f"Total number of customers with transactions: {len(items)}\n")



def most_sold_items(bst):
    print("\n========== BEST SELLING PRODUCTS RANKING ==========")

    # Get all nodes via in-order traversal
    nodes = bst.inorder()

    if not nodes:
        print("Product BST is empty.")
        return

    # ── Sort descending by saled ────
    # Work on a copy of the list to preserve original order
    sorted_nodes = nodes[:]    # shallow copy

    n = len(sorted_nodes)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sorted_nodes[j].saled < sorted_nodes[j + 1].saled:
                sorted_nodes[j], sorted_nodes[j + 1] = sorted_nodes[j + 1], sorted_nodes[j]

    # Print result table
    print(f"\n{'Rank':<6}{'pcode':<10}{'Product name':<25}"
          f"{'Sold':>8}{'Stock':>10}{'Price':>15}")
    print("-" * 76)

    for rank, node in enumerate(sorted_nodes, start=1):
        marker = "  TOP SELLER" if rank == 1 else ""
        print(f"{rank:<6}{node.pcode:<10}{node.pro_name:<25}"
              f"{node.saled:>8}{node.remaining():>10}"
              f"{node.price:>14,.0f}{marker}")

    print("-" * 76)
    print(f"Total number of product types: {n}\n")


def sales_menu(bst, ll_cus, ll_order):
    """
    Sub‑menu for section 4 – Sales Action.
    Called from the main menu (main_menu.py).
    """
    MENU = """
╔══════════════════════════════════════╗
║         4. SALES ACTION              ║
╠══════════════════════════════════════╣
║  4.1  Register sale transaction      ║
║  4.2  Statistics by customer code    ║
║  4.3  Best selling products          ║
║  0.   Back to main menu              ║
╚══════════════════════════════════════╝"""

    while True:
        print(MENU)
        choice = input("Select function: ").strip()

        if choice == "4.1":
            register_sale(bst, ll_cus, ll_order)

        elif choice == "4.2":
            employees_most_sales(ll_order)

        elif choice == "4.3":
            most_sold_items(bst)

        elif choice == "0":
            print("Returning to main menu...")
            break

        else:
            print("[!] Invalid choice. Please try again.")
