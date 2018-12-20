'''
设计一个python程序，建立两个员工数据的环形链表
并将两个链表来连接起来，最后进行打印
'''
import sys

class Employ():
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None

class Opration():
    def __init__(self):
        self.head=Employ()
        self.no_salary1=[[1001,32567],[1002,23455],[1003,34224],[1007,31267],
                    [1012,42660],[1014,25636],[1018,44156],[1043,76542],
                    [1031,32789],[1037,21100],[1041,32196],[1046,25776]]
        self.name1=['we','de','fr','da','fd','gb','wq','as','cd','gt','hy','qa']
        self.no_salary2 = [[1111, 32567], [1112, 23455], [1113, 34224], [1114, 31267],
                           [1115, 42660], [1116, 25636], [1117, 44156], [1118, 76542],
                           [1119, 32789], [1110, 21100], [1121, 32196], [1123, 25776]]
        self.name2 = ['大', '小', '式', '个', '人', '物', '你', '说', '对', '还', '是', '不']

    def add_data(self,no_salary,name):
        head=Employ()
        head.num=no_salary[0][0]
        head.salary=no_salary[0][1]
        head.name=name[0]
        head.next=None
        ptr=head
        for i in range(1,12):
            new_data = Employ()
            if not new_data:
                print('创建内存失败')
                sys.exit()
            new_data.num=no_salary[i][0]
            new_data.salary=no_salary[i][1]
            new_data.name=name[i]
            ptr.next=new_data
            ptr=ptr.next
        ptr.next=head
        return head

    def show(self,head):
        ptr = head
        i=0
        while True:
            print('\t员工编号:{} \t姓名:{} \t\t薪水:{}'
                  .format(ptr.num,ptr.name,ptr.salary))
            i=i+1
            if ptr.next == head :
                break
            ptr = ptr.next
        print('总共{}个数据'.format(i))

    def link_connect(self,head1,head2):
        #将两个链表中的元素相互对调就行
        head=head1.next
        head1.next=head2.next
        head2.next=head
        return head2


    def run(self):
        head1=self.add_data(self.no_salary1,self.name1)
        self.show(head1)
        head2=self.add_data(self.no_salary2,self.name2)
        self.show(head2)
        head=self.link_connect(head1,head2)
        self.show(head)
if __name__ == '__main__':
    opration=Opration()
    opration.run()

