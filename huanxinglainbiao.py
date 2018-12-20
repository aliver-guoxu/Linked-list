'''
环形链表 设计一个程序 可以让用户输入完数据新增学生数据的节点
并建立一个环向链表，当用户输入结束后，可遍历此链表并显示其内容
'''
class Student():
    def __init__(self):
        self.name=''
        self.no=''
        self.next=None

class Opration():
    def __init__(self):
        self.head=Student()
        self.ptr=self.head

    def add_data(self):
        select=0
        while select !=2:
            select=int(input('请输入选项《输入1》《退出2》:'))
            self.ptr.name=input('姓名：')
            self.ptr.no=input('学号：')
            new_data=Student()
            self.ptr.next=new_data
            new_data.next=None
            self.ptr=new_data
        self.ptr.next=self.head
        self.ptr=self.head

    def show(self):
        while True:
            print('学号：{}\t 姓名：{}'.format(self.ptr.no,self.ptr.name))
            self.ptr=self.ptr.next
            if self.ptr.next==self.head:
                break

    def run(self):
        self.add_data()
        self.show()

if __name__ == '__main__':
    opration=Opration()
    opration.run()

