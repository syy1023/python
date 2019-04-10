'''

findall() 会搜索字符串，以列表形式返回全部能匹配的子串。
findall(pattern, string, flags=0)
'''
import re
html='''<div id="songs-list">
    <h2 class="title">测试方法</h2>
    <p class="introduction">
        测试方法
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">黑盒测试</li>
        <li data-view="7">
            <a href="/2.mp3" testway="任贤齐">白盒测试</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" testway="LoadRunner">性能测试</a>
        </li>
        <li data-view="6"><a href="/4.mp3" testway="beyond">接口测试</a></li>
        <li data-view="5"><a href="/5.mp3" testway="陈慧琳">自动化测试</a></li>
        <li data-view="5">
            <a href="/6.mp3" testway="LoadRunner">压力测试</a>
        </li>
    </ul>
</div>'''

result1=re.search('<a.*?testway="(.*?)">(.*?)</a>',html)

print(result1.group(1),result1.group(2))

result2=re.findall('<a.*?testway="(.*?)">(.*?)</a>',html)
print(result2)