def quetion01():
    '''
    设计一个0！-n!的python程序
    :return:
    '''
    sum=1
    num=int(input('请输入一个阶乘：'))
    for i in range(0,num+1):
        for j in range(i,0,-1):
            sum =sum*j
        print('%d!=%04d'%(i,sum))
        sum=1

def question2(i):
    '''
    使用递归来计算一个数的阶乘
    :return:
    '''
    if i==0:
        return 1
    else:
        product=i*question2(i-1)
        return product

def run():
    try:
        num=int(input('请输入要求的阶乘数:'))
    except Exception as e:
        print('输入有误')
    result=question2(num)
    print('%d!=%d'%(num,result))

def hanoi(n,p1,p2,p3):
    if n==1:#递归的出口
        print('盘子从%d移动到了%d'%(p1,p3))
    else:
        hanoi(n-1,p1,p3,p2)
        print('盘子从%d移动到了%d' % (p1, p3))
        hanoi(n-1,p2,p1,p3)
def question3():
    j=int(input('请输入要移动的盘子的数量：'))
    hanoi(j,1,2,3)

if __name__ == '__main__':
    question3()