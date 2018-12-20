'''
设计一个程序，建立一个员工数据的单向链表，并允许删除链表头部/链表中间/链表尾部情况，
最后离开时，显示此链表所有节点的数据字符的内容
'''
import sys

class employee():
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None

class Opration():
    def __init__(self):
        """
        准备需要向链表中传输的数据
        """
        self.position = 0
        self.data = [[1001, 32567], [1002, 23455], [1003, 34224], [1007, 31267],
                     [1012, 42660], [1014, 25636], [1018, 44156], [1043, 76542],
                     [1031, 32789], [1037, 21100], [1041, 32196], [1046, 25776]]
        self.namedata = ['we', 'de', 'fr', 'da', 'fd', 'gbg', 'wq', 'as', 'cd', 'gt', 'hy', 'qa']

    def print_data(self):
        """
        打印准备的额数据
        :return:
        """
        print('员工编号   薪水   员工编号   薪水   员工编号   薪水   员工编号   薪水')
        print('*' * 30)
        for i in range(3):
            for j in range(4):
                print('[%4d] $%5d' % (self.data[j * 3 + i][0], self.data[j * 3 + i][1]), end='  ')
            print()
        print('*' * 30)

    def add_data(self):
        """
        将打印的数据添加到链表中去
        :return:
        """
        self.head=employee() #建立列表头部
        self.head.next=None
        if not self.head:
            print('error，内存分分配失效')
            sys.exit()
        self.head.num=self.data[0][0]
        self.head.name=self.namedata[0]
        self.head.salary=self.data[0][1]
        self.head.next=None
        ptr=self.head
        for i in range(1,12):#建立链表
            newnode=employee()
            newnode.next=None
            newnode.num=self.data[i][0]
            newnode.name=self.namedata[i]
            newnode.salary=self.data[i][1]
            newnode.next=None
            ptr.next=newnode
            ptr=ptr.next

    def del_data(self,ptr):
        """
        删除指定链表中的数据
        :return:
        """
        top=self.head
        if ptr.num == self.head.num:
            #次数表示要删除的节点在头部
            self.head=self.head.next
            print('已删除第{}员工，姓名：{}，薪资：{}'.format(ptr.num,ptr.name,ptr.salary))
        else:
            while top.next !=ptr:#找到删除节点前的位置
                top=top.next
            if ptr.next == None:#删除最后一个节点
                top.next=None
                print('已删除第{}员工，姓名：{}，薪资：{}'.format(ptr.num, ptr.name, ptr.salary))
            else:
                top.next=ptr.next#删除中间的任意节点
                print('已删除第{}员工，姓名：{}，薪资：{}'.format(ptr.num, ptr.name, ptr.salary))
        return self.head

    def change_data(self):
        """
        需要删除的链表
        :return:
        """
        while True:
            print('请输入要删除的员工编号，员工编号必须在列表内部')
            position = int(input('要结束删除过程，请输入-1:'))
            if position == -1:
                break
            else:
                ptr=self.head
                find=0
                while ptr!= None:
                    if ptr.num == position:
                        ptr=self.del_data(ptr)
                        find=find+1
                        self.head=ptr
                    ptr=ptr.next
                if find==0:
                    print('对不起，您输入的编号有误，请重新输入')

    def show_data(self):
        """
        将进行操作后的链表进行展示
        :return:
        """
        ptr=self.head
        print('\t员工编号    姓名\t薪水')
        print('*'*60)
        num=0
        while ptr!= None:
            print('\t[%2d]\t[%-3s]\t[%3d]'%(ptr.num,ptr.name,ptr.salary))
            ptr=ptr.next
            num+=1
        print('总共有{}个数据'.format(num))

    def run(self):
        self.print_data()
        self.add_data()
        self.change_data()
        self.show_data()

if __name__ == '__main__':
    opration=Opration()
    opration.run()