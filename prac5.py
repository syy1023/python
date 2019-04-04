
'''
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive. The string can contain any char.


str1='ooxxc8occbxxx'

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


Instructions
Output
Take 2 strings s1 and s2 including only letters from ato z.
Return a new sorted string, the longest possible, containing distinct letters,


set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
def longest(a1, a2):
    print(set(a1 + a2))
    return "".join(sorted(set(a1 + a2)))


print(longest("aretheyhere","yestheyarehere"))

'''















