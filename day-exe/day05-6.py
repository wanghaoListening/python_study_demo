
"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改
元组中的元素是无法修改的，事实上我们在项目中尤其是多线程环境（后面会讲到）中可能更喜欢使用的是那些不变对象（一方面因为对象状态不能修改，所以可以避免由此
引起的不必要的程序错误，简单的说就是一个不变的对象要比可变的对象更加容易维护；另一方面因为没有任何一个线程能够修改不变对象的内部状态，一个不变对象自动就
是线程安全的，这样就可以省掉处理同步化的开销。一个不变对象可以方便的被共享访问）。所以结论就是：如果不需要对元素进行添加、删除、修改的时候，可以考虑使用
元组，当然如果一个方法要返回多个值，使用元组也是不错的选择。

元组在创建时间和占用的空间上面都优于列表。我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和列表各自占用了多少内存空间，这个很容易做到。
"""

def main():
    #定义元组
    t = ("wanghao",25,"boy","shandong")
    print(t)
    #下标获取元组的元素
    print(t[0])
    print(t[3])
    #遍历元组的值
    for member in t:
        print(member)

    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('tom', 22, "boy", 'NewYork')
    print(t)
    # 将元组转换成列表
    person = list(t)
    person[0] = 'mike'
    print(person)
    #将列表转换成元组
    fruit_list = ['apple','banana','orange']
    fruit_tuple = tuple(fruit_list)
    print(fruit_tuple)


if __name__=='__main__':
    main()