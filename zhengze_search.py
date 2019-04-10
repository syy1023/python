'''

re.search扫描整个字符串并返回第一个成功的匹配。
re.search(pattern, string, flags=0)
'''

import re

str2='hello this is anryan speaking on April 10th 2019'

result1=re.match('anryan.*?(\d+).*',str2)
# match没有匹配, 字符串不是anryan开头

result2=re.search('anryan.*?(\d+).*',str2)
# 而re.search匹配整个字符串，直到找到一个匹配

print(result1)

print(result2.group(1))