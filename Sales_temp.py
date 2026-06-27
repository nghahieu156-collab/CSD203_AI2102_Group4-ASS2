
# ── 4.1 Register Sale ─────────────────────────────────────

def register_sale(bst, ll_cus, ll_order):
    """
    Thực hiện một giao dịch bán hàng:
      1. Kiểm tra ccode tồn tại
      2. Kiểm tra pcode tồn tại
      3. Kiểm tra saled + quantity <= quantity (tồn kho)
      4. Cập nhật saled trong BST
      5. Ghi lại order vào ll_order
    """


# ── 4.2 Employees with most sales ─────────────────────────
# Lưu ý: đề không có bảng nhân viên riêng → mình dùng ccode
# đại diện cho "người bán" trong order list.
# Nếu nhóm muốn tách riêng employees thì có thể mở rộng sau.

def employees_most_sales(ll_order):
    """
    Thống kê ccode nào có tổng quantity bán nhiều nhất
    (xem ccode như đại diện giao dịch).
    """



# ── 4.3 Most sold items ───────────────────────────────────

def most_sold_items(bst):
    """
    Duyệt toàn bộ BST (in-order), lấy saled của từng sản phẩm,
    sắp xếp giảm dần và hiển thị.
    """




