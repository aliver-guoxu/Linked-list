'''
老鼠走迷宫问题
'''
# ============program description==============
# 程序目标 老鼠走出迷宫
class Node():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.next=None

class TraceRecorde():
    def __init__(self):
        self.first=None
        self.last=None

    def isEmpty(self):
        return self.first == None

    def insert(self,x,y):
        newnode=Node(x,y)
        if self.first==None:
            self.first=newnode
            self.last=newnode
        else:
            self.last.next=newnode
            self.last=newnode

    def delete(self):
        if self.first == None:
            print(['队列已经空了'])
            return
        newnode=self.first
        while newnode.next != self.last:
            newnode=newnode.next
        newnode.next=self.last.next
        self.last=newnode

Exitx=8 #定义出口的x坐标在第8行
Exity=10 #定义出口的y坐标在第10行

#声明迷宫
MAZE=[[1,1,1,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,1,1,1,1,1,1,1,1],
      [1,1,1,0,1,1,0,0,0,0,1,1],
      [1,1,1,0,1,1,0,1,1,0,1,1],
      [1,1,1,0,0,0,0,1,1,0,1,1],
      [1,1,1,0,1,1,0,1,1,0,1,1],
      [1,1,1,0,1,1,0,1,1,0,1,1],
      [1,1,1,1,1,1,0,1,1,0,1,1],
      [1,1,0,0,0,0,0,0,1,0,0,1],
      [1,1,1,1,1,1,1,1,1,1,1,1]]

def chkexit(x,y,ex,ey):
    if x==ex and y==ey:
        if (MAZE[x-1][y] ==1 or MAZE[x+1][y] == 1 or MAZE[x][y-1]==1 or MAZE[x][y+1]==2):
            return 1
        if (MAZE[x - 1][y] == 1 or MAZE[x + 1][y] == 1 or MAZE[x][y - 1] == 2 or MAZE[x][y + 1] == 1):
            return 1
        if (MAZE[x - 1][y] == 1 or MAZE[x + 1][y] == 2 or MAZE[x][y - 1] == 1 or MAZE[x][y + 1] == 1):
            return 1
        if (MAZE[x - 1][y] == 2 or MAZE[x + 1][y] == 1 or MAZE[x][y - 1] == 1 or MAZE[x][y + 1] == 1):
            return 1
    return 0
# 主程序
path=TraceRecorde()
x=1
y=1
print('[迷宫的路径（0标记的地方）]')
for i in range(10):
    for j in range(12):
        print(MAZE[i][j],end='')
    print()
while x<=Exitx and y<=Exity:
    MAZE[x][y]=2
    if MAZE[x-1][y] == 0:
        x=x-1
        path.insert(x,y)
    elif MAZE[x+1][y] == 0:
        x=x+1
        path.insert(x,y)
    elif MAZE[x][y-1] ==0:
        y=y-1
        path.insert(x,y)
    elif MAZE[x][y+1]==0:
        y=y+1
        path.insert(x,y)
    elif chkexit(x,y,Exitx,Exity)==1:
        break
    else:
        MAZE[x][y]=2
        path.delete()
        x=path.last.x
        y=path.last.y
print('老鼠走过的路（2标记的地方）')
for i in range(10):
    for j in range(12):
        print(MAZE[i][j],end='')
    print()
