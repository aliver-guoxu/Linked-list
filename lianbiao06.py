"""
设计一个python程序，求出以下两个多项式A（x）+B（x）的值
"""
import sys
class LinkedList():#定义链表结构
    def __init__(self):
        self.coef=0
        self.exp=0
        self.next=None

class Opration():
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2

    def create_link(self,data):
        head = LinkedList()
        if not head:
            print('申请内存失败')
            sys.exit()
        head.coef=data[0]
        head.exp=3
        head.next=None
        ptr=head
        for i in range(1,4):
            new_code = LinkedList()
            if data[i]!=0:
                new_code.coef = data[i]
                new_code.exp = 3 - i
                new_code.next = None
                ptr.next=new_code
                ptr=new_code
        return head

    def print_link(self,head):
        while head != None:
            if head.exp==1 and head.coef!=0:
                print('{}X+'.format(head.coef),end='')
            elif head.exp !=0 and head.coef !=0:
                print('{}X^{}+'.format(head.coef,head.exp),end='')
            elif head.coef!=0:
                print('{}'.format(head.coef),end='')
            head=head.next
        print()

    def sum_link(self,a,b):
        """
        多项式相加
        :param a:
        :param b:
        :return:
        """
        i=0
        ptr=b
        plus=[None]*4
        while a!=None:
            if a.exp == b.exp:
                plus[i]=a.coef+b.coef
                a=a.next
                b=b.next
                i=i+1
            elif b.exp>a.exp:
                plus[i]=b.coef
                b=b.next
                i=i+1
            elif a.exp>b.exp:
                plus[i]=a.coef
                a=a.next
                i=i+1
        return plus

    def run(self):
        head1=self.create_link(self.data1)
        self.print_link(head1)
        head2=self.create_link(self.data2)
        self.print_link(head2)
        plus=self.sum_link(head1,head2)
        head3=self.create_link(plus)
        self.print_link(head3)

if __name__ == '__main__':
    data1=[3,0,4,2]
    data2=[6,8,6,9]
    opration=Opration(data1,data2)
    opration.run()