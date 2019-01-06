'''
设计一个python程序，按序输入一棵树二叉树节点的数据
分别是5，6，24，8，12，3，17，1，9，利用链表来建立二叉树
最后进行中序遍历
'''
class Tree():
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None

class Tree_find():
    def __init__(self):
        self.data=[7,4,1,5,16,8,11,12,15,9,2]
        self.root=None

    def input_data(self):
        for i in range(len(self.data)):
            self.create_tree(self.data[i])

    def create_tree(self,val):
        new_data=Tree()
        new_data.data=val
        new_data.left=None
        new_data.right=None
        if self.root == None:
            self.root=new_data
        else:
            current=self.root
            while current != None:
                backup=current
                if current.data > val:
                    current=current.left
                else:
                    current=current.right
            if backup.data>val:
                backup.left=new_data
            else:
                backup.right=new_data

    def inorder(self,ptr):
        if ptr != None:
            self.inorder(ptr.left)
            print(ptr.data,end=' ')
            self.inorder(ptr.right)

    def forward_order(self,ptr):
        if ptr != None:
            print(ptr.data,end=' ')
            self.forward_order(ptr.left)
            self.forward_order(ptr.right)

    def back_order(self,ptr):
        if ptr != None:
            self.back_order(ptr.left)
            self.back_order(ptr.right)
            print(ptr.data,end=' ')

    def run(self):
        self.input_data()
        ptr = self.root
        print('中序法',end='')
        self.inorder(ptr)
        print('前序法',end='')
        self.forward_order(ptr)
        print('后序法',end='')
        self.back_order(ptr)

if __name__ == '__main__':
    trees=Tree_find()
    trees.run()