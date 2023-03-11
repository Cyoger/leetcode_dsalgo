class node:
    
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.key = data
        
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=' ')
            
    def preorder(self, root):
        if root:
            print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
            
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)
            
            

