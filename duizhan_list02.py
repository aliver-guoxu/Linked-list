'''
设计一个python程序，以数组仿真扑克牌洗牌及发牌的过程。使用随机数
来生成扑克牌放入堆栈，放满52张拍后开始发牌，使用堆栈功能来给4个人发牌
'''
import random

class Stack_list():

    def __init__(self):
        self.maxstack = 52
        self.satck = [None] * self.maxstack
        self.top = -1  # 堆栈的顶端

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, value):
        if self.top > self.maxstack - 1:
            print('堆栈满了')
        else:
            self.top += 1
            self.satck[self.top] = value

    def pop(self):
        if self.is_empty() == True:
            print('堆栈是空的，无法弹出元素')
        else:
            data = self.satck[self.top]
            print('弹出的元素为{}'.format(data))
            self.top = self.top - 1

    def input_data(self):
        card=[None]*52
        i = 0
        while i != 52:#将52张牌放入堆栈中
            card[i]=i+1
            i+=1
        return card

    def shuffle(self,duizhan):
        print('洗牌中==================')
        result=[]
        while duizhan:
            p=random.randrange(0,len(duizhan))
            result.append(p)
            duizhan.pop(p)
        return result

    def deal(self):
        print('逆时针发牌')
        print('【显示各家的牌】 东家\t 北家\t 西家\t 南家')
        print('='*30)
        while self.top >= 0:
            style=(self.satck[self.top])%4
            if style==0:
                ascval='梅花'
            if style==1:
                ascval='方块'
            if style==2:
                ascval='红桃'
            if style==3:
                ascval='黑桃'
            print('[%s%3d]\t'%(ascval,self.satck[self.top]%13+1),end='')
            if self.top%4==0:
                print()
            self.top-=1

    def put_duizhan(self,card):
        for i in card:
            self.push(i)

    def run(self):
        card=self.input_data()
        card_new=self.shuffle(card)
        self.put_duizhan(card_new)
        self.deal()








if __name__ == '__main__':
    stack_list = Stack_list()
    stack_list.run()