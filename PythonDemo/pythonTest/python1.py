# 生成器(返回迭代器的函数)
# yield: 每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值
import sys


def fibonacci(n):  # 生成器函数　－　斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


def printIterator(f): # 打印迭代器
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()


# 返回迭代器的生成器
def iterateNum(startnum,totalcount):
    while True:
        if startnum > totalcount:
            return
        yield startnum
        startnum += 1


# 打印螺旋矩阵
# 性能问题：　由于采用的逐步遍历,所以当n无限大的时候时间会边长
def luoxuanjuzhen(n):
    start_num = 1
    num = getTotalFloor(n)
    itr = iterateNum(start_num, num)
    array = [[0 for i in range(n)] for i in range(n)]

    # 记录当前到达的矩阵位置
    begin_num = 0
    # 行长度
    length = n
    x = 0
    y = 0
    while True:
        try:
            # 获取当前层数
            circle_num = next(itr)
            # 获取当前层数数字总数
            total_num = getFloorNum(circle_num, n)
            i = 0
            while i < total_num:
                begin_num += 1
                i = i + 1
                # 判断当前元素是矩阵中第几行第几列
                x = getx(length, i)
                y = gety(length, i)
                if x > 0 and y > 0:
                    array[x+circle_num-2][y+circle_num-2] = begin_num
                # print("层数:"+circle_num+",当前层数总数："+total_num, end='\n')
            length -= 2
        except StopIteration:
            array_num = 0
            # 打印矩阵
            for item in array:
                for a in item:
                    # 此处格式化输出应改为根据最大数值进行初始化
                    print("%3d"%a, end=' ')
                    array_num += 1
                    if array_num%n == 0:
                        print("\n")
            sys.exit()


# 获取矩阵总层数
def getTotalFloor(n):
    totalFloor = 0
    while True:
        if n <= 0:
            return totalFloor
        totalFloor += 1
        n -= 2


# 获取矩阵总长度
def getLength(n):
    return n*n


# 获取矩阵层数对应的数字总数
def getFloorNum(num:dict(type=int, help='矩阵层数'), n:dict(type=int,help='矩阵阶数')):
    length = n-2*(num-1)
    if length == 1:
        return 1
    elif length < 1:
        return 0
    else:
        return (length-1)*4


# 获取数字在矩阵中的位置y
def gety(n:"行长度", num:"当前位置"):
    if n > 1:
        if num <= n:
            return num
        elif (num > n) and (num <= 2 * n - 1):
            return n
        elif (num > 2 * n - 1) and (num <= 3*n - 2):
            return 3*n-num-1
        elif num > 3*n-2:
            return 1
    elif n == 1:
        return 1
    else:
        return 0


# 获取数字在矩阵中的位置x
def getx(n, num):
    if n > 1:
        if num <= n:
            return 1
        elif (num > n) and (num <= 2 * n - 1):
            return num-n+1
        elif (num > 2 * n - 1) and (num <= 3*n - 2):
            return n
        elif num > 3*n-2:
            return 4*n-num-2
    elif n == 1:
        return 1
    else:
        return 0


luoxuanjuzhen(6)
#f = fibonacci(10)  # f是一个迭代起,由生成器返回
#printIterator(f);