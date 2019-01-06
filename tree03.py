'''
实现一个二叉树的查找程序，首先建立一个二叉查找树，并输入要查找的值
如果节点中有相等的值，就会显示出查找的次数，如果找不到这个值，也会
显示出相关信息
'''
class Tree():
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None

class Tree_find():
    def __init__(self):
        self.data=[7,1,4,2,8,13,12,11,15,9,5]
        self.root=None

    def input_data(self):
        for i in range(len(self.data)):
            self.create_tree(self.data[i])

    def create_tree(self,val):
        '''
        建立查找二叉树
        :param val:
        :return:
        '''
        new_data=Tree()
        new_data.data=val
        new_data.left=None
        new_data.right=None
        if self.root == None:
            self.root=new_data
        else:
            backup=self.root
            # 把指针移动到最后
            while backup != None:
                current=backup
                if backup.data > val:
                    backup=backup.left
                else:
                    backup=backup.right

            if val > current.data:
                current.right=new_data
            else:
                current.left=new_data

    def check_data(self):
        '''
        对输入的值在二叉树中进行查找
        :return:
        '''
        num=int(input('请输入要查找的数值：'))
        i=1
        if self.root == None:
            print('您需要查找的二叉树为空，请添加数据后在进行查找')
        else:
            ptr=self.root
            while True:
                i=i+1
                if ptr == None:#必须放在最前面
                    print('找了{}次，但是没找打，我已经尽力了'.format(i))
                    break
                elif num > ptr.data:
                    ptr=ptr.right
                elif num < ptr.data:
                    ptr=ptr.left
                elif num == ptr.data:
                    print('找到了，总共找了{}次'.format(i))
                    break

    def order_ouput(self,ptr):
        '''
        中序输出
        :param ptr:
        :return:
        '''
        if ptr != None:
            self.order_ouput(ptr.left)
            print(ptr.data)
            self.order_ouput(ptr.right)

    def run(self):
        self.input_data()
        ptr=self.root
        self.order_ouput(ptr)
        self.check_data()

if __name__ == '__main__':
    trees=Tree_find()
    trees.run()