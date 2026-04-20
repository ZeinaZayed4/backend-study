# Trees

## Binary Trees

- A binary tree is a hierarchical data structure where each node has at most two children, called left and right
- **Root:** the topmost node.
- **Parent/internal node:** any node that has at least one child node (not a leaf).
- **Child node:** a node that is directly connected and one level below a parent node.
- **Leaf node:** a node that has no children.
- **Sibling nodes:** nodes that share the same parent.
- **Height:** the height of a tree is the number of nodes on the longest path from root to leaf.
- **Descendant:** a descendant of a node is any node that lies in its subtree.
- **Ancestor:** an ancestor of a node is any node on the path from that node up to the root.
- **Depth:** the depth of a node is the number of nodes from the root to that node.
- Binary trees do not contain cycles.

- 
    ```java
    class TreeNode {
        int val;
        TreeNode left = null;
        TreeNode right = null;

        TreeNode(int val) {
            this.val = val;
        }
    }
    ```
- 
    ```py
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    ```

## Binary Search Trees (BST)

- A BST is a binary tree in which for each node, all values in the left subtree are less than the node, and all values in the right subtree are greater.
- Complexity: **O(log n)** in balanced BST, but **O(n)** in the worst case.
    ```py
    def search(root, target):
        if not root:
            return False
        
        if target > root.val:
            return search(root.right, target)
        elif target < root.val:
            return search(root.left, target)
        else:
            return True
    ```
- Inserting and deleting can be **O(log n)** on average, but **O(n)** in the worst case.

### BST - Insert

- 
    ```py
    def insert(root, val):
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = insert(root.right, val)
        elif val < root.val:
            root.left = insert(root.left, val)
        return root
    ```

### BST - Remove

- We need to find the minimum.
    ```py
    def min_value_node(root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    ```
- Case 1: Node has 0 children (leaf): simply remove it (return None).
- Case 2: Node has 1 child: replace the node with its child.
- Case 3: Node has 2 children:
    - Find the smallest in right subtree.
    - Replace node value with it.
    - Delete the smallest node.
    ```py
    def remove(root, val):
        if not root:
            return None

        if val > root.val:
            root.right = remove(root.right, val)
        elif val < root.val:
            root.left = remove(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = min_value_node(root.right)
                root.val = min_node.val
                root.right = remove(root.right, min_node.val)
        return root
    ```

### Depth-First-Search (DFS)

- All DFS traversals (inorder, preorder, postorder, reverse): **O(n)**
- inorder:
    ```py
    def inorder(root):
        if not root:
            return

        inorder(root.left)
        print(root.val)
        inorder(root.right)
    ```
- preorder:
    ```py
    def preorder(root):
        if not root:
            return

        print(root.val)
        preorder(root.left)
        preorder(root.right)
    ```
- postorder:
    ```py
    def postorder(root):
        if not root:
            return

        postorder(root.left)
        postorder(root.right)
        print(root.val)
    ```
- reverse_inorder:
    ```py
    def reverse_inorder(root):
        if not root:
            return

        reverse_inorder(root.right)
        print(root.val)
        reverse_inorder(root.left)
    ```

### Breadth-First-Search (BFS)

- **O(n)**
    ```py
    from collections import deque

    
    def bfs(root):
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            print(f"Level: {level}")
            for _ in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
    ```

### Sets and Maps

- Sets and maps are commonly implemented using BST.
- 
    ```py
    from sortedcontainers import SortedDict

    treeMap = SortedDict({"c": 3, "a": 1, "b": 2})
    ```
