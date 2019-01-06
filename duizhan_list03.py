'''
使用链表结构来设计一个python程序，用循环来控制元素
压入堆栈或者弹出堆栈，并仿真堆栈的各种操作，此堆栈堆栈最多可容纳100个元素
其中必须包括压入与弹出操作，最后并输出堆栈内的所有元素
'''
class Link():
    '''
    定义链表
    '''
    def __init__(self):
        self.data=None
        self.next=None


class Stack_list():
    def __init__(self):
        self.stack=Link()
        self.stack.next=None
        self.ptr=self.stack

    def is_empty(self):
        if self.stack is None:
            return False
        else:
            return True

    def push(self,value):
        new_data=Link()
        new_data.data=value
        new_data.next=self.stack
        self.stack=new_data

    def pop(self):
        if self.is_empty() == False:
            print('堆栈是空的，无法弹出元素')
        else:
            if self.stack.next != None:
                data=self.stack.data
                self.stack=self.stack.next
                print(data)
            else:
                print('取完了')

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
        self.input_data()

if __name__ == '__main__':
    stack_list=Stack_list()
    stack_list.run()