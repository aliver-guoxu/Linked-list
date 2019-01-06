'''
设计一个python程序，使用堆栈法来将所输入的中序法
表达式转换成后续法表达式
'''
class InToPost():
    def __init__(self):
        max=50
        self.index=-1
        self.stack_t=[None]*max #定义堆栈
        self.infx=['']*50 #定义转化后储存列表
        self.infx_priority=['']*9
        self.stack_priority=['']*8
        self.infx_priority[0]='q'
        self.infx_priority[1]=')'
        self.infx_priority[2]='+'
        self.infx_priority[3]='-'
        self.infx_priority[4]='*'
        self.infx_priority[5]='/'
        self.infx_priority[6]='^'
        self.infx_priority[7]=''
        self.infx_priority[8]='('
        self.stack_priority[0] = 'q'
        self.stack_priority[1] = ')'
        self.stack_priority[2] = '+'
        self.stack_priority[3] = '-'
        self.stack_priority[4] = '*'
        self.stack_priority[5] = '/'
        self.stack_priority[6] = '^'
        self.stack_priority[7] = ''

    def compare(self,stack_0,infix_0):
        index_s=0
        index_i=0
        while self.stack_priority[index_s] != stack_0:
            index_s+=1
        while self.infx_priority[index_i] !=infix_0:
            index_i+=1
        if int(index_s/2)>=int(index_i/2):
            return 1
        else:
            return 0

    def convert(self):
        top=0
        flag=0
        self.stack_t[top]='q'
        stack=self.stack_t
        infx=self.infx
        for flag in range(self.index+2):#循环index次
            if self.infx[flag]==')':#当碰到‘）’时 将‘（’之前的运算符全部输出
                while self.stack_t[top]=='(':
                    print('%c'%self.stack_t[top],end='')
                    top-=1
            elif self.infx[flag]=='q':
                while self.stack_t[top]!='q':
                    print('%c' % self.stack_t[top],end='')
                    top-=1
            elif self.infx[flag]=='(' or self.infx[flag]=='^'or self.infx[flag]=='*' or self.infx[flag]=='/' or self.infx[flag]=='+' or self.infx[flag]=='-':
                while self.compare(self.stack_t[top],self.infx[flag])==1:
                    print('%c' % self.stack_t[top],end='')
                    top-=1
                top+=1
                self.stack_t[top]=self.infx[flag]
            else:
                print('%c' % self.infx[flag],end='')

    def input_data(self):
        '''
        输入表达式，并将表达式按从左向右的顺序进行储存到self.infx中去
        :return:
        '''
        input_data=str(input('请输入中序表达式：'))
        i=0
        while i<len(input_data):
            self.index=self.index+1
            self.infx[self.index]=input_data[i]
            i+=1
        self.infx[self.index+1]='q'

    def run(self):
        self.input_data()
        self.convert()

if __name__ == '__main__':
    intopost=InToPost()
    intopost.run()