class Tree():
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None

class Tree_find():
    def __init__(self):
        self.data=[5,6,24,8,12,3,17,1,9]
        self.root=None

    def input_data(self):
        for i in range(9):
            val=self.data[i]
            self.create_tree(val)

    def create_tree(self,val):
        new_code=Tree()
        new_code.data=val
        new_code.left=None
        new_code.right=None
        if self.root == None:
            self.root=new_code
        else:
            current=self.root
            while current != None:#将指针最后一个地方
                backup = current
                if current.data > val:
                    current=current.left
                else:
                    current=current.right
            if backup.data > val:
                backup.left=new_code
            else:
                backup.right=new_code

    def show(self):
        print('='*20)
        print('左子树')
        left=self.root.left
        while left !=None:
            print(left.data)
            left=left.left
        print('='*20)
        print('右子树')
        right=self.root.right
        while right !=None:
            print(right.data)
            right=right.right

    def run(self):
        self.input_data()
        self.show()

if __name__ == '__main__':
    tree=Tree_find()
    tree.run()
