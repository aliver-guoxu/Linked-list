'''
设计一个程序，将员工数据的链表节点按照工号反转打印
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
            newnode.num=self.data[i][0]
            newnode.name=self.namedata[i]
            newnode.salary=self.data[i][1]
            newnode.next=None
            ptr.next=newnode
            ptr=ptr.next

    def change_data(self):
        """
        对链表进行反转
        :return:
        """
        ptr=self.head
        self.pre=None
        last=None

        while ptr != None:
            last=self.pre
            self.pre=ptr
            ptr=ptr.next
            self.pre.next=last

    def show_data(self):
        """
        将进行操作后的链表进行展示
        :return:
        """
        ptr=self.pre
        print('\t员工编号\t\t姓名\t\t薪水')
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