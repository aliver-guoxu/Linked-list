'''
使用数组结构来设计一个python程序，用循环来控制元素
压入堆栈或者弹出堆栈，并仿真堆栈的各种操作，此堆栈堆栈最多可容纳100个元素
其中必须包括压入与弹出操作，最后并输出堆栈内的所有元素
'''
class Stack_list():

    def __init__(self):
        self.maxstack=100
        self.satck=[None]*self.maxstack
        self.top=-1#堆栈的顶端

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self,value):
        if self.top > self.maxstack-1:
            print('堆栈满了')
        else:
            self.top+=1
            self.satck[self.top]=value

    def pop(self):
        if self.is_empty() == True:
            print('堆栈是空的，无法弹出元素')
        else:
            data=self.satck[self.top]
            print('弹出的元素为{}'.format(data))
            self.top=self.top-1

    def input_data(self):
        i=2
        count=0
        while True:
            i=int(input('要压入堆栈请输入1，要弹出堆栈请输入0，要停止操作请输入-1：'))
            if i== -1:
                break
            elif i== 1:
                value=int(input('请输入元素的值：'))
                self.push(value)
            elif i==0:
                self.pop()

    def run(self):
        pass

if __name__ == '__main__':
    stack_list=Stack_list()
    stack_list.run()