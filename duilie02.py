'''
使用链表结构来设计一个python程序，链表中的元素节点仍为学生的姓名及成绩、
本程序还包含队列的加入/取出/遍历的操作
'''
class Link():
    def __init__(self):
        self.name=None
        self.score=None
        self.next=None

class Duilie():
    def __init__(self):
        self.link=Link()
        self.font=None
        self.rear=None

    def opration(self):
        select=0
        while True:
            select=input('请输入你的选择《1》添加《2》取出《3》显示《4》离开:')
            if select == '1':
                name=input('请输入学生的名称：')
                score=input('请输入学生的成绩：')
                self.enquene(name,score)
            elif select == '2':
                self.dequene()
            elif select == '3':
                self.show()
            elif select == '4':
                break
            else:
                print('请按照提示进行操作')

    def enquene(self,name,score):
        if self.font == None:
            self.link.name=name
            self.link.score=score
            self.link.next=None
            self.font=self.link
            self.rear=self.link
        else:
            new_data=Link()
            new_data.name=name
            new_data.score=score
            new_data.next=None
            self.rear.next=new_data
            self.rear=self.rear.next
            self.font=self.link

    def dequene(self):
        if self.font== None:
            print('队列还是空的呢，别着急等会在取')
        elif self.font != None:
            print('姓名{}成绩{}'.format(self.font.name,self.font.score))
            self.font=self.font.next
            if self.font==None:
                self.link = Link()
            else:
                self.link=self.font

    def show(self):
        ptr=self.font
        if ptr == None :
            print('队列是空的。。。。别着急')
        else:
            while ptr != None:
                print('姓名{}成绩{}'.format(ptr.name,ptr.score))
                ptr=ptr.next

    def run(self):
        self.opration()

if __name__ == '__main__':
    duilie=Duilie()
    duilie.run()