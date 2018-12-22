'''
设计一个python程序，可以输入学生的相关数据，使用双向链表进行储存
，等到输入完成后，进行打印
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

    def input_data(self):
        select=0
        while select != 2:
            select=int(input('如果继续请输入1，如果退出请输入2：'))
            self.name=input('请输入姓名：')
            self.salary=input('请输入薪资：')
            self.no=input('请输入学号：')
            self.age=input('请输入年龄：')
            self.add_data(self.name,self.salary,self.no,self.age)

    def add_data(self,name,salary,no,age):
        new_data=Employ()
        if not new_data:
            print('分配内存失败')
        new_data.age=age
        new_data.salary=salary
        new_data.no=no
        new_data.name=name
        self.ptr.rlink=new_data
        new_data.rlink=None
        new_data.llink=self.ptr
        self.ptr=new_data

    def show(self):
        ptr=self.head.rlink
        while ptr != None:
            print('学号：{}，薪水：{}，年龄{}，姓名{}'.format(
                ptr.no,ptr.salary,ptr.no,ptr.name
            ))
            ptr=ptr.rlink

    def run(self):
        self.input_data()
        self.show()

if __name__ == '__main__':
    opration=Opration()
    opration.run()


