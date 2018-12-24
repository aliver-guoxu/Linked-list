'''
设计一个python程序来实现环形队列的操作
当要取出数据是可输入0，要结束的时候可输入-1
'''
class Cduilie():
    def __init__(self):
        self.max=5
        self.quene=['']*self.max
        self.front=-1
        self.rear=-1

    def input_data(self):
        select=4
        while True:
            select=int(input('插入《0》取出《1》显示《2》退出《3》：'))
            if select==0:
                val=input('请输入需要插入的数据：')
                self.enquene(val)
            if select==1:
                self.dequene()
            if select==2:
                self.show()
            if select==3:
                break

    def enquene(self,val):
        '''压入队列'''
        if self.rear+1==self.front or self.rear == self.max-1 and self.front<=0:
            print('队列已满')
        else:
            self.rear = self.rear + 1
            if self.rear == self.max:
                self.rear=0
            self.quene[self.rear]=val

    def dequene(self):
        if self.rear == self.front:
            print('队列已空，请先放入数据')
        else:
            self.front = self.front + 1
            if self.front == self.max:
                self.front=0
            print('弹出的数据为：%s'%self.quene[self.front])

    def show(self):
        print('剩余的元素为：')
        if self.rear==self.front:
            print('剩余的元素为空')
            return
        a=self.front
        while self.rear != a:
            a=a+1
            if a==5:
                a=0
            print('[{}]'.format(self.quene[a]))

    def run(self):
        self.input_data()

if __name__ == '__main__':
    cduilie=Cduilie()
    cduilie.run()