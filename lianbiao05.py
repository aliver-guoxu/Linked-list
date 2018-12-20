'''
设计一个python程序，建立者5个学生成绩单的单向链表
然后遍历每一个节点并全部打印出来
'''
import sys

class employee():
    def __init__(self):
        self.num=0
        self.grade=0
        self.name=''
        self.next=None

class Opration():

    def __init__(self):
        self.head = employee()
        self.head.next=None

    def input_data(self):
        self.num=input('请输入学生的学号<一次性输入五项，用","分割>：').split(',')
        self.grade=input('请输入学生的成绩<一次性输入五项，用","分割>：').split(',')
        self.name=input('请输入学生的姓名<一次性输入五项，用","分割>:').split(',')

    def write(self):
        if not self.head:
            print('内存分配失效')
            sys.exit()
        self.head.num = self.num[0]
        self.head.grade = self.grade[0]
        self.head.name = self.name[0]
        ptr=self.head

        for i in range(1,5):
            self.newd = employee()
            if not self.newd:
                print('内存分配失效')
                sys.exit()
            self.newd.num=self.num[i]
            self.newd.grade=self.grade[i]
            self.newd.name=self.name[i]
            self.newd.next=None
            ptr.next=self.newd #把新的节点加到链表的后面
            ptr=ptr.next #将指针一道链表的最后一个节点

    def output(self):
        ptr=self.head
        while ptr != None:
            print('学号{}，姓名{}，成绩{}'.format(
                ptr.num,ptr.name,ptr.grade))
            ptr=ptr.next

    def run(self):
        self.input_data()
        self.write()
        self.output()

if __name__ == '__main__':
    opration=Opration()
    opration.run()
