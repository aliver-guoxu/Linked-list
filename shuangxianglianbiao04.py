'''
设计一个python程序，建立一个员工的双向链表
允许删除链表的头部 链表的中间部位以及链表的尾部，并在
最后进行显示删除后的内容
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

    def input_data(self):
        select=0
        while select != 2:
            select=int(input('如果继续请输入1，如果退出请输入2：'))
            position=int(input('请输入需要删除节点的位置：'))
            ptr=self.find_node(position)
            self.delete_data(ptr)

    def find_node(self,position):
        ptr=self.head
        while ptr!= None:
            if ptr.no == position:
                return ptr
            ptr=ptr.rlink
        return ptr

    def delete_data(self, find_ptr):
        ptr=self.head
        print(find_ptr.no)
        if self.head ==  None:
            print('链表已经空了 再删了')
        else:
            if find_ptr ==  self.head:
                self.head=self.head.rlink
                self.head.llink=None

            elif find_ptr.rlink == None:
                #删除尾节点
                find_ptr.llink.rlink=None

            else:
                #删除中间节点
                find_ptr.llink.rlink=find_ptr.rlink
                find_ptr.rlink.llink=find_ptr.llink

    def add_data(self):
        self.head.no=self.no_salary[0][0]
        self.head.salary=self.no_salary[0][1]
        self.head.name=self.name[0]
        self.head.age=self.age[0]
        for i in range(1,12):
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
                ptr.no,ptr.salary,ptr.age,ptr.name
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


