# -*- coding: cp936 -*-
from pylab import *
import binascii
import re
import sys

# pythonĬ�ϵĵݹ�����Ǻ����޵ģ������900������ӣ����ݹ���ȳ������ֵ��ʱ��
# �ͻ�����������һ���쳣(RuntimeError: maximum recursion depth exceeded in cmp),����ķ�ʽ���ֹ����õݹ������ȣ���ʽΪ
sys.setrecursionlimit(1000000)  # ������������Ϊһ����

print("*" * 100)
with open(r"C:\Users\hp\Desktop\mRNAhot.txt", 'r', encoding="utf-8") as f:
    data = f.read()
    ff = data.replace('\n', '')
    partern = 'AAG'
    for m in re.finditer(partern, ff):
        print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
    l = len(ff)
    # print(ff)
    # print(l)
with open(r"C:\Users\hp\Desktop\myfile.txt", 'a', encoding="utf-8") as myfile:
    # �ҳ���Խṹ�������ṹ����ʼ�ͽ���λ�ô�ӡ��myfile��
    def RNA(n, g):
        i = 1
        sumk = 0
        while ((i < l - g) and (n - i >= 0) and (
                (ff[n - i] == 'A' and ff[n + g - 1 + i] == 'U') or (ff[n - i] == 'U' and ff[n + g - 1 + i] == 'A') or (
                ff[n - i] == 'U' and ff[n + g - 1 + i] == 'G') or (ff[n - i] == 'C' and ff[n + g - 1 + i] == 'G') or (
                        ff[n - i] == 'G' and ff[n + g - 1 + i] == 'C') or (ff[n - i] == 'G' and ff[n + g - 1 + i] == 'U'))):
            sumk = sumk + 1
            if (sumk >= 2):
                # print(sumk)
                s = ff[n - i:n + g + i]
                # print('The number of pairs=',sumk-1)
                # print(s)
                if (sumk - 1) >= 3:
                    myfile.write(str(n - i) + ' ')
                    myfile.write(str(n + g + i - 1) + '\n')

            else:
                continue
            i = i + 1
            # continue
        else:
            return i

    # ָ��gap
    for g in range(0, 7):
        for k in range(2, l - 11):
            RNA(k, g)
    print("*" * 100)

# ����ʼ�ͽ���λ������һ��ֿ�
with open(r"C:\Users\hp\Desktop\myfile.txt", 'r', encoding="utf-8") as f:
    line = f.read()
    LL = line.split()
    c = len(LL) / 2
    print(c)
    print(LL)
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
        mm = mm + 2
        nn = nn + 2
        sande.append(dd)
    print(sande)

    # ������Խṹ��Ϊ1
    j = 0
    while j < c:
        start = int(sande[j][0])
        end = int(sande[j][1])
        a = end - start + 1
        #    print ff[start:end+1]
        ff = ff.replace(ff[start:end + 1], '1' * a)
        j = j + 1

    # ����Ե�Ϊ0
    for y in range(0, l):
        if ff[y] != '1':
            ff = ff.replace(ff[y], '0')

    # ������ʺͶ���Ei��������=-0.5
    y = ff.count('1')
    z = ff.count('0')

    p = float(y) / l
    q = 1 - p

    s = (-0.5 - p) / q

    def fac(n):
        if n == 0:
            return 0
        else:
            # return n*fac(n-1)
            if ff[n] == '1':

                return max(fac(n - 1) + 1, 0)
            else:
                return max(fac(n - 1) + s, 0)


    # ����Ei�Ľ��
    v = []
    for m in range(0, l):
        # ��������ӵ��б���
        v.append(fac(m))
    print(v)

    plot(v)
    show()


