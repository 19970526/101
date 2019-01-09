import re

text = '1111Python'

res = re.findall(r'(?<=[0-9]{4})\w+(?=[a-z]{4})', text)
print(res)
