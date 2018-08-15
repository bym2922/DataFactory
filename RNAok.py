# -*- coding: cp936 -*-
from pylab import *
import binascii
import re
import sys
# python默认的递归深度是很有限的，大概是900多的样子，当递归深度超过这个值的时候，
# 就会引发这样的一个异常(RuntimeError: maximum recursion depth exceeded in cmp),解决的方式是手工设置递归调用深度，方式为
sys.setrecursionlimit(1000000)            # 例如这里设置为一百万

myfile = open(r"K:\RNA\myFile6.txt", 'w')  # 新建空文件
F = open(r"C:\Users\hp\Desktop\mRNAhot.txt")              # 打开序列文件
aa = F.readlines()                                         # 读取文件内容
# print aa
# print aa[0]
aa.pop(0)
# print aa
dd = ''.join(aa)
# print dd
ff = dd.replace('\n', '')

l = len(ff)

# print ff
print("*"*100)

# 找出配对结构，并将结构的起始和结束位置打印在myfile1中


def RNA(n, g):
    i = 1
    sumk = 0
    while ((i < l - g)and(n - i >= 0)and((ff[n-i] == 'A' and ff[n+g-1+i] == 'U')or(ff[n-i] == 'U' and ff[n+g-1+i] == 'A')or(ff[n-i] == 'U' and ff[n+g-1+i] == 'G')or(ff[n-i]=='C' and ff[n+g-1+i]=='G')or(ff[n-i] == 'G' and ff[n+g-1+i] == 'C')or(ff[n - i] == 'G' and ff[n+g-1+i] == 'U'))):
        sumk = sumk + 1
        if(sumk >= 2):
            print(sumk)
            s = ff[n-i:n+g+i]
            # print('The number of pairs=',sumk-1)
            if (sumk-1) >= 3:
                
                myfile.write(str(n-i)+'\n')
                myfile.write(str(n+g+i-1)+'\n')

        else:
            continue
        i = i+1
        continue
    else:
        return i
# 指定gap
for g in range(0,7):
    for k in range(2, l-11):
        RNA(k, g)


myfile.close()
print("*"*100)



# 将起始和结束位置两个一组分开

f = open(r"K:\RNA\myFile6.txt")
line = f.read()             
f.close()

LL = line.split()
c = len(LL)/2
# print c
# print LL
'''
def group(LL, n):
    num = len(LL) % n
    zipped = zip(*[iter(LL)] * n)
    return zipped if not num else zipped + [LL[-num:], ]
    #return zipped
 
sande = group(LL, 2)
#print sande
'''
mm = 0
nn = 2
sande = []
while nn <= len(LL):
    dd = LL[mm:nn]
    mm = mm+2
    nn = nn+2
    sande.append(dd)
# print sande



# d = open(r'C:\Users\hp\Desktop\124.txt')
# aa = d.read()
# d.close()

# fff = aa.replace('\n', '')
# L = len(fff)
# print fff
# print L
# print "*************************************"

# print sande[0][0]

# 出现配对结构的为1
j = 0
while j < c:
    # print j
    start = int(sande[j][0])
#    print start
    end = int(sande[j][1])
#    print end

    a = end-start+1

#    print ff[start:end+1]
    ff = ff.replace(ff[start:end+1],'1'*a)
    
#    print ff

    j = j+1

#不配对的为0
for y in range(0, l):
    if ff[y] != '1':
        ff = ff.replace(ff[y], '0')
#        print ff

# 算出概率和定义Ei函数，μ=-0.5
y = ff.count('1')
z = ff.count('0')
# print y
# print z

p = float(y)/l
q = 1-p

# print 'p=',p

s = (-0.5-p)/q
# print 's=',s


def fac(n):
    if n == 0:
        return 0
    else:
        # return n*fac(n-1)
        if ff[n] == '1':
            
            return max(fac(n-1)+1, 0)
        else:
            return max(fac(n-1)+s, 0)

#各个Ei的结果       
v = []
for m in range(0, l):
    # print fac(m)
    # 将数据添加到列表中
    v.append(fac(m))
    # print v

    
#    print ss
print(v)

plot(v)
show()


