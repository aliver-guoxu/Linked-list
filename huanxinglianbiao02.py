'''
设计一个python程序，建立一个员工数据的环形链表
并允许在链表的头部和中间插入新节点，最后离开时，列出链表的最后所有节点的
的数据字段的内容
'''
import sys

class Employ():
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None

class Opration():
    def __init__(self):
        self.head=Employ()
        self.no_salary=[[1001,32567],[1002,23455],[1003,34224],[1007,31267],
                    [1012,42660],[1014,25636],[1018,44156],[1043,76542],
                    [1031,32789],[1037,21100],[1041,32196],[1046,25776]]
        self.name=['we','de','fr','da','fd','gb','wq','as','cd','gt','hy','qa']

    def add_data(self):
        self.head.num=self.no_salary[0][0]
        self.head.salary=self.no_salary[0][1]
        self.head.name=self.name[0]
        self.head.next=None
        self.ptr=self.head
        for i in range(1,12):
            new_data = Employ()
            if not new_data:
                print('创建内存失败')
                sys.exit()
            new_data.num=self.no_salary[i][0]
            new_data.salary=self.no_salary[i][1]
            new_data.name=self.name[i]
            self.ptr.next=new_data
            self.ptr=self.ptr.next
        self.ptr.next=self.head

    def find_node(self,position):
        '''
        找到需要插入的点
        :param position:
        :return:
        '''
        ptr=self.head
        while ptr.next != self.head:
            if ptr.num == position:
                return ptr
            ptr=ptr.next
        print('执行了到最后一个节点了')
        return ptr

    def insert_data(self,ptr):
        print('ptr当前的位置',ptr.num)
        print('ptr',ptr.next.num)
        print('head',self.head)
        insert=Employ()
        if not insert:
            print('分配内存失败')
            sys.exit()
        insert.num=self.new_num
        insert.salary=self.new_salary
        insert.name=self.new_name
        insert.next=None
        cur=self.head
        if ptr.next == self.head:
            #如果在头部插入
            insert.next=self.head
            while cur.next != self.head:
                cur=cur.next
            cur.next=insert
            self.head=insert
        else:
            #指针不再头部的情况
            print('BUS')
            insert.next=ptr.next
            ptr.next=insert

    def input_data(self):
        while True:
            print('请输入要插入员工的编号（学号相同的话不能重复插入）')
            position=int(input('学生编号,如果退出的话编号为-1:'))
            if position == -1:
                break
            ptr=self.find_node(position)
            self.new_num=int(input('请插入学生的编号：'))
            self.new_salary=int(input('请插入学生的薪水：'))
            self.new_name=input('请输入学生的姓名：')
            self.insert_data(ptr)

    def show(self):
        ptr = self.head
        i=0
        while True:
            print('\t员工编号:{} \t姓名:{} \t\t薪水:{}'
                  .format(ptr.num,ptr.name,ptr.salary))
            i=i+1
            if ptr.next == self.head :
                break
            ptr = ptr.next
        print('总共{}个数据'.format(i))
    def run(self):
        self.add_data()
        self.show()
        self.input_data()
        self.show()

if __name__ == '__main__':
    opration=Opration()
    opration.run()

