class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif self.data:
                if data>self.data:
                    if self.right is None:
                        self.right=node(data)
                    else:
                        self.right.insert(data)
        else:
            self.data=data
    def print(self):
        print(self.data)
        if self.left:
            self.left.print()
       
        if self.right:
            self.right.print()

lst=[int(i) for i in input().split()]
root=node(lst[0])
for i in lst[1:]:
    root.insert(i)
root.print()
        
