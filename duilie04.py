'''
使用链表设计一个python程序来实现一个限制的双向队列，我们只能从一段加入
数据，但可以从队列中取出数据时，可以分别从前端以及末端取数据
'''
class Dlink():
    def __init__(self):
        self.data=0
        self.next=None

class Cduilie():
    def __init__(self):
        self.head=Dlink()
        self.front=None
        self.rear=None

    def input_data(self):
        select=4
        while True:
            select=int(input('插入《0》取出《1》显示《2》退出《3》：'))
            if select==0:
                val=input('请输入需要插入的数据：')
                self.enquene(val)
            if select==1:
                self.dequene(action=1)
                self.dequene(action=2)
            if select==2:
                self.show()
            if select==3:
                break

    def enquene(self,val):
        if self.front==None:
            self.head.data=val
            self.front = self.head
            self.rear = self.head
        else:
            new_data=Dlink()
            new_data.data=val
            self.rear.next=new_data
            self.rear=self.rear.next

    def dequene(self,action):
        if self.front == None:
            print('队列为空。。。。。。')
        elif self.front != None and action==1:
            print('从首部取出来的数据为{}'.format(self.front.data))
            self.front=self.front.next
        elif self.front != None and action==2:
            print('从尾部取出来的数据为{}'.format(self.rear.data))
            ptr=self.head
            while ptr.next != self.rear and ptr.next !=None:
                ptr=ptr.next
                print(ptr.data)
            self.rear=ptr #将指针移动到rear的前一个节点

    def show(self):
        ptr=self.front
        if ptr==None:
            print('队列为空')
        else:
            while ptr != self.rear:
                print('[%s]'%ptr.data)
                ptr=ptr.next

    def run(self):
        self.input_data()

if __name__ == '__main__':
    cduilie=Cduilie()
    cduilie.run()