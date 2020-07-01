import re
a = "123abc456"
print (re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)+re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))  