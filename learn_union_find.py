# coding:utf-8
import re
import time


class UF_quickfind:
    def __init__(self, N):
        self.N = N
        self.aid = range(N)

    def connected(self, p, q):
        if self.aid[p] == self.aid[q]:
            return True
        else:
            return False

    def union(self, p, q):
        idp = self.aid[p]
        idq = self.aid[q]
        for x in xrange(self.N):
            if self.aid[x] == idq:
                self.aid[x] = idp

class UF_quickunion:
    def __init__(self, N):
        self.N = N
        self.aid = range(N)

    def root(self, x):
        while True:
            bid = self.aid[x]
            if bid == x:
                return bid
            else:
                x = bid

    def union(self, p, q):
        if not self.connected(p, q):
            self.aid[p] = self.aid[q]

    def connected(self, p, q):
        if self.root(p) == self.root(q):
            return True
        else:
            return False





def readfile(filepath):
    with open(filepath) as a:
        global Na
        Na = int(a.readline())
        print Na
        b = re.findall(r"(\d+)\t(\d+)", a.read())
        assert b is not None, "RE ERROR"
        return b


def gofile(b,classname):
    uf = classname(Na)
    for p, q in b:
        intp = int(p)
        intq = int(q)
        if not uf.connected(intp, intq):
            uf.union(intp, intq)
            print intp, "union", intq


starttime = time.time()
Na = 0
x = readfile("uftest.txt")
gofile(x, UF_quickfind)
print time.time() - starttime


starttime = time.time()
x = readfile("uftest.txt")
gofile(x, UF_quickunion)
print time.time() - starttime
