'''
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
re.match(pattern, string, flags=0)
'''

import re
str1="My 123 name is anryan and now I am working in thoughtworks for less than year"

#print(re.match('My',"My 123 name is anryan and now I'm working in thoughtworks").span())
#print(re.match('My',"My name is anryan and now I'm working in thoughtworks"))


# "^Hello " 匹配字符串开头; (\d+) 匹配任意个数字; .* 匹配任意字符(换行符除外);
# String$ 匹配字符串结尾




result2=re.match('.*(\d+).*',str1)
## 使用.*匹配其他所有字符, (\d+)匹配我们想要的数字,贪婪模式，匹配出的是数字的个数
print(result2.group(1))


result3=re.match('.*？(\d+).*',str1)
print(result3.group(1))


