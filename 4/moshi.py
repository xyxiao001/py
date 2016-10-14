import re

# 搜索字符串
match = re.match('Hello[ \t]*(.*)world', 'Hello  Python world')
print(match.group(1))

match2 = re.match('/(.*)/(.*)/(.*)', '/usr/home/xyxiao')
print(match2.groups())
