import re
import collections
content = "Hello 123 4567 World_This i128763876`12s a Regex Demo"

print(len(content))

result = re.match('^H.*?(\d+)\s(\d+).*mo$', content)



print(result)
# print(result.group(1), end = '')
print(result.group(1) + result.group(2))
print(type(result.group(1) + result.group(2)))
