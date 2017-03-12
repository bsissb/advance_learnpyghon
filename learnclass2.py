# coding:utf-8

# 定义一个列表的操作类：Listinfo
# 包括的方法:
# 1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
# 2 列表元素取值：get_key(num) [num:整数类型]
# 3 列表合并：update_list(list)	  [list:列表类型]
# 4 删除并且返回最后一个元素：del_key()
class Listinfo:
    def __init__(self, alist):
        self.alist = alist

    def add_key(self, keyname):
        assert isinstance(keyname, int) or isinstance(keyname, str), "Error, not a str or int"
        self.alist.append(keyname)

    def get_key(self, num):
        assert isinstance(num, int), "Error ,not add a int"
        return self.alist[num]

    def update_list(self, blist):
        assert isinstance(blist, list), "Error ,not update a list"
        self.alist.extend(blist)

    def del_key(self):
        x = self.alist.pop()
        return x

    def get_list(self):
        return self.alist


list_info = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])
list_info.add_key("aefarer")
print list_info.get_key(4)
list_info.update_list(["ab",323])
print list_info.del_key()
print list_info.get_list()

# 定义一个集合的操作类：Setinfo
# 包括的方法:
# 1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
# 2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
# 3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
# 4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
class Setinfo:
    def __init__(self, aset):
        assert isinstance(aset, set), "Error, not a set"
        self.aset = aset

    def add_setinfo(self, keyname):
        self.aset.add(keyname)

    def get_intersection(self, unioninfo):
        assert isinstance(unioninfo, set)
        return self.aset | unioninfo

    def get_union(self, unioninfo):
        assert isinstance(unioninfo, set)
        return self.aset & unioninfo

    def del_difference(self, unioninfo):
        assert isinstance(unioninfo, set)
        return self.aset - unioninfo
# set_info =  Setinfo(你要操作的集合)
