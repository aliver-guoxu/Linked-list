import sys
'''
设计一个python程序来实现队列的操作，加入数据时输入a
要取出元素时可输入d，并直接打印出队列前端的值，要结束的话则输入e
'''

class Duilie():

    def __init__(self):
        self.max=10
        self.quene=[None]*self.max
        self.rear=-1 #尾部增加一个元素 其+1
        self.font=-1 #每取出一个元素 其+1

    def opration(self):
        op=None
        while self.rear<self.max and op !='e':
            op=str(input('如果需要添加数据请输入a，删除数据请输入d，退出请输入e：'))
            if op == 'a':
                val=int(input('请输入需要添加的数据：'))
                self.add(val)
            elif op == 'd':
                self.delete()
            elif op == 'e':
                print('结束了')
                break
            else:
                print('请按照提示输入相对应的操作符')

    def add(self,val):
        if self.rear+1<self.max:
            self.rear=self.rear+1
            self.quene[self.rear]=val
        else:
            print('不好意思队列已经满了，不能继续添加了')

    def delete(self):
        if self.rear>self.font:
            self.font = self.font + 1
            print('取出来的数据为{}'.format(self.quene[self.font]))
        else:
            print('已经取完了取不出来了')


    def run(self):
        self.opration()
        print(self.quene)

if __name__ == '__main__':
    duilie=Duilie()
    duilie.run()