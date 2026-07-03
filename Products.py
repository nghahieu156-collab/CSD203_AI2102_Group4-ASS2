"""
Nguyen Ha Hieu
DATE: 26/06/2006"""

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

    # insert: new product
    def insert(self, pcode, pro_name, quantity, saled, price):
        node = ProductNode(pcode, pro_name, quantity, saled, price)
        if self.root is None: # if none = root
            self.root = node
            return True
        cur = self.root
        while True: # loop for compare  new pcode, current pcode
            if pcode == cur.pcode: 
                return False          # duplicate
            elif pcode < cur.pcode:   # turn left if smaller
                if cur.left is None:
                    cur.left = node
                    return True
                cur = cur.left
            else: 
                if cur.right is None:
                    cur.right = node
                    return True
                cur = cur.right

    # find product
    def search(self, pcode):
        cur = self.root
        while cur:
            if pcode == cur.pcode:
                return cur
            if pcode < cur.pcode:
                cur = cur.left
            else:
                cur = cur.right
        return None

    # ── in-order (returns sorted list) ──────
    def inorder(self, node=None, first=True):
        if first:
            node = self.root
        result = []
        if node:
            result += self.inorder(node.left, False)
            result.append(node)
            result += self.inorder(node.right, False)
        return result

    # ── BFS (KHÔNG DÙNG deque) ──────
    def bfs(self):
        if not self.root:
            return []
            
        result = []
        q = [self.root]
        
        head = 0  # Dùng con trỏ head thay cho q.popleft() để duyệt mảng
        size = 1  # Biến theo dõi kích thước mảng (thay thế hàm len())
        
        while head < size:
            node = q[head]
            head += 1
            result.append(node)
            
            if node.left:
                q.append(node.left)
                size += 1
            if node.right:
                q.append(node.right)
                size += 1
        return result

    # delete by copying
    def delete(self, pcode):
        parent, cur, is_left = None, self.root, False
        while cur and cur.pcode != pcode:
            parent = cur
            if pcode < cur.pcode:
                cur, is_left = cur.left, True
            else:
                cur, is_left = cur.right, False
                
        if cur is None:
            return False

        # Case: two children => copy successor
        if cur.left and cur.right:
            succ_parent, succ = cur, cur.right
            while succ.left:
                succ_parent, succ = succ, succ.left
            # copy data
            cur.pcode    = succ.pcode
            cur.pro_name = succ.pro_name
            cur.quantity = succ.quantity
            cur.saled    = succ.saled
            cur.price    = succ.price
            # delete successor (has at most right child)
            child = succ.right
            if succ_parent is cur:
                succ_parent.right = child
            else:
                succ_parent.left  = child
        else:
            if cur.left is None:
                child = cur.right
            else:
                child = cur.left
                
            if parent is None:
                self.root = child
            elif is_left:
                parent.left = child
            else:
                parent.right = child
        return True

    # ── count ──────
    def count(self, node=None, first=True):
        if first:
            node = self.root
        if node is None:
            return 0
        return 1 + self.count(node.left, False) + self.count(node.right, False)

    # ── height (KHÔNG DÙNG max()) ──────
    def height(self, node=None, first=True):
        if first:
            node = self.root
        if node is None:
            return 0
            
        left_h = self.height(node.left, False)
        right_h = self.height(node.right, False)
        
        # Tự so sánh để thay cho hàm max()
        if left_h > right_h:
            return 1 + left_h
        else:
            return 1 + right_h

    # ── simple balancing (KHÔNG DÙNG len()) ──────
    def balance(self):
        nodes = self.inorder()
        
        # Tự đếm số lượng phần tử thay vì dùng len(nodes)
        node_count = 0
        for _ in nodes:
            node_count += 1
            
        self.root = self._sorted_to_bst(nodes, 0, node_count - 1)

    def _sorted_to_bst(self, nodes, lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = nodes[mid]
        node.left  = self._sorted_to_bst(nodes, lo, mid - 1)
        node.right = self._sorted_to_bst(nodes, mid + 1, hi)
        return node

    # ── update saled ──────
    def update_saled(self, pcode, qty):
        node = self.search(pcode)
        if node is None:
            return False, "Product not found"
        if node.saled + qty > node.quantity:
            return False, f"Not enough stock (remaining={node.remaining()})"
        node.saled += qty
        return True, "OK"
