'''
设计一个程序，可以让用户输入数据新增学生数据节点，并建立一个单向链表
当用户输入结束后，可遍历此链表并显示其内容，并求出当前链表中所有学生的数学和英语的
平均成绩
'''
import sys
class Student():
    def __init__(self):
        self.name=''
        self.math=0
        self.eng=0
        self.no=''
        self.next=None
head=Student()
head.next=None
ptr=head
Msum=Esum=num=student_no=0
select=0
while select !=2:
    print('(1)新增（2）离开=》')
    try:
        select=int(input('请输入一个选项:'))
    except ValueError:
        print('输入错误')
        print('请重新输入')

    if select==1:
        new_data=Student()
        new_data.name=input('姓名')
        new_data.no=input('学号')
        new_data.math=eval(input('数学成绩'))
        new_data.eng=eval(input('英语成绩'))
        ptr.next=new_data
        new_data.next=None
        ptr=ptr.next
        num=num+1

ptr=head.next
print()
while ptr!=None:
    print('姓名{},学号{}，数学成绩{}，英语成绩{}'.format(
        ptr.name,ptr.no,ptr.math,ptr.eng))
    Msum=Msum+ptr.math
    Esum=Esum+ptr.eng
    student_no=student_no+1
    ptr=ptr.next

if student_no != 0:
    print('学生的应数学平均分数为{}，学生的英语成绩为{}'.format(
        Msum/student_no,Esum/student_no
    ))
