class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class bst:
    def addnode(self,root, val):
        if root==None:
            root=Node(val)
            return root
        else:
            if val>root.data:
                root.right=self.addnode(root.right,val)
            else:
                root.left= self.addnode(root.left,val)

        return root
    #****----------------------------------------------------------------****
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data,end=" ")
        if root.right!=None:
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        pass
        

    def levelorder(self,root):
        if root==None:
            return
        else:
            q=[root]
            while q:
                x=q.pop(0)
                print(x.data,end=' ')
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                    
        

li=[16,9,25,4,10,8,83,35]
tree=bst()
root=tree.addnode(None,li[0])
for i in range(1,len(li)):
    root=tree.addnode(root,li[i])

print("inorder:")
tree.inorder(root)
print()
print()
print("preorder:")
tree.preorder(root)
print()
print("level order:")
tree.levelorder(root)
