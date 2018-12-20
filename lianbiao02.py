'''
设计一个程序，建立一个员工数据的单向链表，并允许在链表头部/链表中间/链表尾部插入
新节点的情况，最后离开时，显示此链表所有节点的数据字符的内容
'''
import sys

class employee():
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None

def findone(head,num):
    ptr=head
    while ptr != None:
        if ptr.num==num:
            return ptr
        ptr=ptr.next
    return ptr

def insertnode(head,ptr,num,salary,name):
    InserNode=employee()
    if not InserNode:
        return None
    InserNode.num=num
    InserNode.salary=salary
    InserNode.name=name
    InserNode.next=None
    if ptr == None: #插入头节点
        InserNode.next=head
        return InserNode
    else:
        if ptr.next==None:#插入尾节点
            ptr.next=InserNode
        else:#插入中间节点
            InserNode.next=ptr.next
            ptr.next=InserNode
    return head

position=0
data=[[1001,32567],[1002,23455],[1003,34224],[1007,31267],
      [1012,42660],[1014,25636],[1018,44156],[1043,76542],
      [1031,32789],[1037,21100],[1041,32196],[1046,25776]]
namedata=['we','de','fr','da','fd','gbg','wq','as','cd','gt','hy','qa']
print('员工编号   薪水   员工编号   薪水   员工编号   薪水   员工编号   薪水')
print('*'*30)
for i in range(3):
    for j in range(4):
        print('[%4d] $%5d'%(data[j*3+i][0],data[j*3+i][1]),end='  ')
    print()
print('*'*30)

head=employee() #建立列表头部
head.next=None
if not head:
    print('error，内存分分配失效')
    sys.exit()
head.num=data[0][0]
head.name=namedata[0]
head.salary=data[0][1]
head.next=None
ptr=head
for i in range(1,12):#建立链表
    newnode=employee()
    newnode.next=None
    newnode.num=data[i][0]
    newnode.name=namedata[i]
    newnode.salary=data[i][1]
    newnode.next=None
    ptr.next=newnode
    ptr=ptr.next

while True:
    print('请输入要插入其后的员工编号，如输入的编号不再此列表中')
    position=int(input('请输入员工节点将视为此链表的链表头部，要结束插入过程，请输入-1:'))
    if position==-1:
        break
    else:
        ptr=findone(head,position)
        new_num=int(input('请输入员工的编号:'))
        new_salary=int(input('请输入员工的薪水:'))
        new_name=input('请输入员工的姓名:')
        head=insertnode(head,ptr,new_num,new_salary,new_name)
    print()

ptr=head
print('\t员工编号    姓名\t薪水')
print('*'*60)
num=0
while ptr!= None:
    print('\t[%2d]\t[%-3s]\t[%3d]'%(ptr.num,ptr.name,ptr.salary))
    ptr=ptr.next
    num+=1
print('总共有{}个数据'.format(num))


