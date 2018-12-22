'''
设计一个python程序，建立一个员工的双向链表
允许在链表的头部 链表的中间部位以及链表的尾部插入数据，并在最后进行显示
'''
class Employ():
    def __init__(self):
        self.name=''
        self.salary=0
        self.no=0
        self.age=0
        self.llink=None
        self.rlink=None

class Opration():
    def __init__(self):
        self.head=Employ()
        self.ptr=self.head
        self.no_salary = [[1001, 32567], [1002, 23455], [1003, 34224], [1007, 31267],
                          [1012, 42660], [1014, 25636], [1018, 44156], [1043, 76542],
                          [1031, 32789], [1037, 21100], [1041, 32196], [1046, 25776]]
        self.name = ['we', 'de', 'fr', 'da', 'fd', 'gb', 'wq', 'as', 'cd', 'gt', 'hy', 'qa']
        self.age=[i for i in range(1,13)]
        print(self.age)
    def input_data(self):
        select=0
        while select != 2:
            select=int(input('如果继续请输入1，如果退出请输入2：'))
            position=int(input('请输入需要插入节点的位置：'))
            ptr=self.find_node(position)
            self.name=input('请输入姓名：')
            self.salary=input('请输入薪资：')
            self.no=input('请输入学号：')
            self.age=input('请输入年龄：')
            self.insert_data(self.name,self.salary,self.no,self.age,ptr)

    def find_node(self,position):
        ptr=self.head
        while ptr != None:
            if ptr.no == position:
                return ptr
            ptr=ptr.rlink
        return ptr

    def insert_data(self, name, salary, no, age,find_ptr):
        ptr=self.head
        insert=Employ()
        insert.name=name
        insert.salary=salary
        insert.no=no
        insert.age=age
        if find_ptr == self.head:
            #头部节点
            ptr.llink=insert
            insert.rlink=ptr
            insert.llink=None
            self.head=insert
            print('修改后头部的值变为{}'.format(self.head.no))

        else:
            if find_ptr.rlink == None:
                #尾部
                find_ptr.rlink=insert
                insert.llink=find_ptr
                insert.rlink=None

            else:
                #插入中间部位
                find_ptr.rlink.llink=insert
                insert.rlink=find_ptr.rlink
                insert.llink=find_ptr
                find_ptr.rlink=insert

    def add_data(self):
        for i in range(12):
            new_data = Employ()
            if not new_data:
                print('分配内存失败')
            new_data.age=self.age[i]
            new_data.salary=self.no_salary[i][1]
            new_data.no=self.no_salary[i][0]
            new_data.name=self.name[i]
            self.ptr.rlink=new_data
            new_data.rlink=None
            new_data.llink=self.ptr
            self.ptr=new_data
        return self.head

    def show_right(self,head):
        print('---------向右遍历节点---------')
        ptr=self.head
        print('首节点是{}'.format(ptr.no))
        i=0
        while ptr != None:
            num=ptr.no
            print('学号：{}，薪水：{}，年龄{}，姓名{}'.format(
                ptr.no,ptr.salary,ptr.no,ptr.name
            ))
            ptr=ptr.rlink
            i=i+1
        print('链表中共有{}个元素'.format(i))

    def run(self):
        head=self.add_data()
        # self.show_right()
        data=self.input_data()
        self.show_right(data)

if __name__ == '__main__':
    opration=Opration()
    opration.run()


