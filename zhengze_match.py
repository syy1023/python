'''
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
re.match(pattern, string, flags=0)

可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
group(num=0)     匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组
groups()       返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
'''

import re
str1="My 123 name is anryan and now I am working in thoughtworks for less than year"

str2='''this is a testing string for zhengze
expression over 5 times
'''

#print(re.match('My',"My 123 name is anryan and now I'm working in thoughtworks").span())
#print(re.match('My',"My name is anryan and now I'm working in thoughtworks"))


# "^Hello " 匹配字符串开头; (\d+) 匹配任意个数字; .* 匹配任意字符(换行符除外);
# String$ 匹配字符串结尾




result2=re.match('.*(\d+).*',str1)
# 使用.*匹配其他所有字符, (\d+)匹配我们想要的数字,贪婪模式，匹配出的是数字的个数
print(result2.group(1))


result3=re.match('.*?(\d+).*',str1)
# 在 .* 后面加 ? 就可以使用非贪婪模式,返回的是具体的字符串
print(result3.group(1))

result4=re.match('.*(\d+).*',str2,re.S|re.I)
print(result4.group(1))
#匹配多行字符，re.S设置'.'可以匹配换行符, re.I忽略大小写


